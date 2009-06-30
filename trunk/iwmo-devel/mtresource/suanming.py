#coding=utf-8
'''
    需要重写的东西：
        类属性
        render方法
'''
import sys
sys.path.append('/home/workspace/gftop/iwmo-devel')
import datetime, urllib, random
import settings
from utils import mdb
from twisted.web.client import getPage
from twisted.web import resource
from twisted.python import logfile
#from mttemplates.kaokaoni import tk as kaokaonitk        考考你题目
import time

currentmonth = datetime.datetime.today().month
log = logfile.DailyLogFile('kaokaoni.mo.log', settings.LOGPATH, defaultMode=0777)
mtlog = logfile.DailyLogFile('kaokaoni.mt.log', settings.LOGPATH, defaultMode=0777)

def getok(result):
    print result
def getfailure(failure):
    print failure
   
    

from mttemplates.suanming.steps import MTsteps
from utils import proxycache, common
import re
re_step = re.compile('^\d+$')


class Suanming(resource.Resource):
    """算命6步同步接口
    
    配置参数说明
    pid: 产品编号, int
    nid: 通道网关编号, int
    cmd: 通道指令, string
    cmd_length: 指令长度, int
    o2: 答题编号, string or int
    response_delay: 是否延迟返回接口, boolean
    response_value: 接口打印信息, string
    mt_send_url:  sp下行地址, url
    mt_step_model:  MT信息调用类, class
    mt_encoding: sp接口编码
    
    
    
    def render(self):
        pass
    
完整示例

class Receive(KaoKaoni):
pid = "18"
nid = "310"
cmd = "8"
cmd_length = len(cmd)
ln = "1062376618"
o2 = "-1"
response_delay = False
response_value = "0"

mt_encodeing = "utf-8"
mt_send_url = "http://59.42.254.185/smscprecv/smsSend.jsp?UserName=ZhiMengDT&Password=zm#dt&Phone=%(phone)s&ToPhone=%(phone)s&Msg=%(mtmsg)s&ServiceId=%(serviceid)s&SpNumber=%(spnumber)s&LinkId=%(linkid)s"
mt_send_timeout = 5
mt_step_model = MT9Mixin

isLeaf = True

def render(self, request):
    self.serviceid = request.args.get('ServiceId', [''])[0]
    self.phone = request.args.get('Phone', [None])[0]
    self.msg = request.args.get('Msg', [''])[0]
    self.spnumber = request.args.get('SpNumber', ['1062376618'])[0]
    self.linkid = request.args.get('LinkId', [None])[0]
    
    _logmsg = '%s: %s\r\n' % (
        datetime.datetime.today(), 
        common.args2str(request.args)
    )
    log.write(_logmsg)        

    if len(self.msg) > self.cmd_length:
        self.o2 = self.msg[self.cmd_length]
        
    if self.phone and self.linkid and self.msg and self.msg.startswith(self.cmd):
        mtstep_key = "%s|%s" % (self.nid, self.phone)
        self.request_mtstep(
            request, 
            mtstep_key,
            phone=self.phone,
            linkid = self.linkid,
            serviceid = self.serviceid,
            spnumber = self.spnumber
        )
        
        if self.response_delay:
            return server.NOT_DONE_YET
        
        return self.response_value
    return self.response_value
    """
    
    pid = "18"
    nid = "268"
    cmd = "11"
    cmd_length = len(cmd)
    ln = ""
    #o2 = "-1"
    response_delay = False
    response_value = "ok"
    
    mt_encodeing = "gbk"
    mt_send_url = "http://218.25.10.21:7000/lf/201_new.asp?phone=%(phone)s&msgcontent=%(mtmsg)s&serviceup=%(serviceup)s&linkid=%(linkid)s&ext=%(ext)s"
    mt_send_timeout = 5
    mt_step_model = MTsteps
    
    isLeaf = True
    
    def render(self, request):
        self.serviceid = request.args.get('ServiceId', [''])[0]
        self.phone = request.args.get('Phone', [None])[0]
        self.msg = request.args.get('Msg', [''])[0]
        self.spnumber = request.args.get('SpNumber', ['1062376618'])[0]
        self.linkid = request.args.get('LinkId', [None])[0]
        
        _logmsg = '%s: %s\r\n' % (
            datetime.datetime.today(), 
            common.args2str(request.args)
        )
        log.write(_logmsg)        
    
        if len(self.msg) > self.cmd_length:
            self.o2 = self.msg[self.cmd_length]
            
        if self.phone and self.linkid and self.msg and self.msg.startswith(self.cmd):
            mtstep_key = "%s|%s" % (self.nid, self.phone)
            self.request_mtstep(
                request, 
                mtstep_key,
                phone=self.phone,
                linkid = self.linkid,
                serviceid = self.serviceid,
                spnumber = self.spnumber
            )
            
            if self.response_delay:
                return server.NOT_DONE_YET
            
            return self.response_value
        return self.response_value

    
    def request_mtstep(self, request, mtstep_key, **kwargs):
        '''请求下行的步数'''
        d = proxycache.pcache.perform("getmtstep", mtstep_key)
        d.addCallback(self._got_mtstep_ok)
        d.addErrback(self._got_mtstep_error)
        d.addCallback(self.mt_send, request, mtstep_key, **kwargs)
        return d   
            
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
        mtt = self.mt_step_model(
            phone=self.phone, 
            step=mtstep, 
            cmd=self.cmd, 
            o2=self.o2
        )
        print 'mtstep=', mtstep
        
        mt_defer = mtt.render()
        mt_defer.addCallback(self._mt_result, request, mtstep_key, **kwargs)
        mt_defer.addErrback(self._mt_result_error, request, mtstep_key, **kwargs)
        
        #设置返回类型
        if self.response_delay:
            mt_defer.addCallback(self.sendmtmsg_to_sp, request, mtstep_key, **kwargs)
        else:
            mt_defer.addCallback(self.sendmt_to_sp, request, mtstep_key, **kwargs)
            
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
    
    
    def sendmtmsg_to_sp(self, result, request, mtstep_key, **kwargs):
        """在接口上返回流程信息供SP抓取"""
        isincr, mtmsg = result
        mtmsg = unicode(mtmsg, 'utf-8').encode(self.mt_encodeing)
        
        if isincr:
            self.incrmtstep(mtstep_key)
            
        request.write(mtmsg)
        request.finish()
        
        
    def sendmt_to_sp(self, result, request, mtstep_key, **kwargs):
        """请求SP下行接口下发"""
        isincr, mtmsg = result
        mtmsg = unicode(mtmsg, 'utf-8').encode(self.mt_encodeing)
        kwargs.update( {'mtmsg': urllib.quote(mtmsg)} )
        
        mturl = self.mt_send_url % kwargs
        
        starttime = time.time()
        d = getPage(mturl, timeout=self.mt_send_timeout)
        d.addCallback(self.req_ok, mturl, starttime, isincr, mtstep_key)
        d.addErrback(self.req_failure, mturl, starttime, isincr, mtstep_key)
        
        return d
    
    def incrmtstep(self, mtstep_key):
        """Update user netgate step"""
        def _incr_success(result):
            print result
        def _incr_failure(failure):
            print failure
        

        d = proxycache.pcache.perform("incrmtstep", mtstep_key)
        d.addCallback(_incr_success)
        d.addErrback(_incr_failure)
        
    
    def req_ok(self, result, mturl, starttime, isincr, mtstep_key):
        """请求SP下行接口成功"""
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
    
