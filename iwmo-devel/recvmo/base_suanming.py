#coding=utf-8
import datetime,urllib,random
import sys
sys.path.append('/home/workspace/gftop/iwmo-devel')
import settings
from utils import mdb
from twisted.web.client import getPage
from twisted.web import resource
from twisted.python import logfile
import time

currentmonth = datetime.datetime.today().month
log = logfile.DailyLogFile('suanming.mo.log', settings.LOGPATH, defaultMode=0777)
mtlog = logfile.DailyLogFile('suanming.mt.log', settings.LOGPATH, defaultMode=0777)

def getok(result):
    print result
def getfailure(failure):
    print failure


from mttemplates.suanming.steps import MT
from utils import proxycache, common
import re
re_step = re.compile('^\d+$')
class Receive(resource.Resource):
    def __init__(self):
        self.nid = 268
        self.pid = 15

    def render(self, request):
        self.phone = request.args.get('phone', [None])[0]
        self.msg = request.args.get('msgcontent', [''])[0]
        self.linkid = request.args.get('linkid', [None])[0]
        self.serviceup = request.args.get('serviceup', ['100'])[0]
        self.ext = request.args.get('ext', ['7'])[0]

        _msg = '%s: %s\r\n' % (
            datetime.datetime.today(),
            common.args2str(request.args)
        )
        log.write(_msg)

        self.cmd = '802' #发送的指令
        self.ln = '1062666777' #用户上行号码
        self.cmd_length = len(self.cmd)

#        self.o2 = '-1'   #用户的选择判断
#        if len(self.msg) > self.cmd_length:
#            self.o2 = self.msg[self.cmd_length]



        if self.phone and self.linkid and self.msg and self.msg.startswith(self.cmd):
            mtstep_key = "%s|%s" % (self.nid, self.phone)
            d = proxycache.pcache.perform("getmtstep", mtstep_key)
            d.addCallback(self._got_mtstep_ok)
            d.addErrback(self._got_mtstep_error)
            d.addCallback(self.mt_send,
                request,
                mtstep_key,
                phone=self.phone,
                linkid=self.linkid,
                serviceup=self.serviceup,
                ext=self.ext
            )
            return "0"
        return "-1"

    def _got_mtstep_ok(self, step):
        """用户发送步骤"""
        return step

    def _got_mtstep_error(self, failure):
        """失败默认为0"""
        step = "0"
        return step

    def mt_send(self, mtstep, request, mtstep_key, **kwargs):
        """下发MT信息"""
        if not re_step.match(mtstep):
            mtstep = 0
        mtstep = int(mtstep)+1
        mtt = MT(
            phone=self.phone,
            step=mtstep,
            cmd=self.cmd,
            o2=self.o2
        )

        print kwargs
        mt_defer = mtt.render()
        mt_defer.addCallback(self._mt_result, request, mtstep_key, **kwargs)
        mt_defer.addErrback(self._mt_result_error, request, mtstep_key, **kwargs)
        mt_defer.addCallback(self.sendmt_to_sp, mtstep_key, **kwargs)
        return "success"


    def _mt_result(self, result, request, mtstep_key, **kwargs):
        """用户短信发送正确,返回流程信息
        isincr: (boolean)是否更新流程判断
        """
        mtmsg = result.strip()
        isincr = True
        return (isincr, mtmsg)

    def _mt_result_error(self, failure, request, mtstep_key, **kwargs):
        """处理用户发送错误指令，返回错误流程信息
        isincr: (boolean)是否更新流程判断
        """
        mtmsg = failure.getErrorMessage()
        isincr = False
        return (isincr, mtmsg)

    def sendmt_to_sp(self, result, mtstep_key, **kwargs):
        """请求SP下发"""
        isincr, mtmsg = result
        mtmsg = unicode(mtmsg, 'utf-8').encode('gbk')
        kwargs.update( {'mtmsg': urllib.quote(mtmsg)} )

        _mturl = 'http://218.25.10.21:7000/lf/201_new.asp?phone=%(phone)s&msgcontent=%(mtmsg)s&serviceup=%(serviceup)s&linkid=%(linkid)s&ext=%(ext)s'
        mturl = _mturl % kwargs

        starttime = time.time()
        d = getPage(mturl, timeout=5)
        d.addCallback(self.req_ok, mturl, starttime, isincr, mtstep_key)
        d.addErrback(self.req_failure, mturl, starttime, isincr, mtstep_key)

        return d

    def incrmtstep(self, mtstep_key):
        def _incr_success(result):
            pass
        def _incr_failure(failure):
            pass
        d = proxycache.pcache.perform("incrmtstep", mtstep_key)
        d.addCallback(_incr_success)
        d.addErrback(_incr_failure)


    def req_ok(self, result, mturl, starttime, isincr, mtstep_key):
        """请求成功"""
        endtime = time.time()
        result = result.strip()

        costime = endtime-starttime
        _msg = '%s,OK: %s||costime=%s||%s\r\n' % (
            datetime.datetime.today(),
            mturl,
            costime,
            result.strip()
        )
        mtlog.write(_msg)

        if isincr:
            self.incrmtstep(mtstep_key)
        print result

    def req_failure(self, failure, mturl, starttime, isincr, mtstep_key):
        """请求失败"""
        endtime = time.time()
        costime = endtime-starttime
        _msg = '%s,FAILURE: %s||costime=%s||%s\r\n' % (
            datetime.datetime.today(),
            mturl,
            costime,
            failure.getErrorMessage()
        )
        mtlog.write(_msg)
        print failure

