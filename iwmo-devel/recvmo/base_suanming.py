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
log = logfile.DailyLogFile('suanming.mo.log', settings.LOGPATH, defaultMode = 0777)
mtlog = logfile.DailyLogFile('suanming.mt.log', settings.LOGPATH, defaultMode = 0777)

def getok(result):
    print result
def getfailure(failure):
    print failure

from utils import proxycache,common
#import re
#re_step = re.compile(r'^\d+$')
class Receive(resource.Resource):
    def __init__(self):
        self.nid = 999        #通道编号
        self.pid = 888        #产品编号
    def render(self,request):
        self.phone = request.args.get('phone', [None])[0]
        self.msg = request.args.get('msgcontent', [''])[0]
        self.linkid = request.args.get('linkid', [None])[0]
        self.serviceup = request.args.get('serviceup', ['100'])[0]
        self.ext = request.args.get('ext', ['7'])[0]

        _msg = '%s: %s\r\n'%(
            datetime.datetime.today(),
            common.args2str(request.args)
        )
        log.write(_msg)

        self.cmd = '802'  #发送的指令
        self.ln = '1062666777'  #用户上行号码
        self.cmd_length = len(self.cmd)

        #self.o2 = '-1'    #用户的选择判断
        if len(self.msg) > self.cmd_length:       #发送短信的内容长度大于指令的长度
            self.o2=self.msg[self.cmd_length]
        if self.phone and self.linkid and self.msg and self.msg.startswith(self.cmd):
            mtstep_key='%s|%s'%(self.nid,self.phone)
            '''
                    先留着后面补上
            '''
            return '0'
        return '-1'
    def mt_send(self,request,**kwargs):
        '''下发MT信息'''
        pass
    def sendmt_to_sp(self,result,**kwargs):
        '''请求sp下发'''
        mtmsg=unicode(mtmsg,'utf-8').encode('gbk')
        kwargs.update({'mtmsg':urllib.quote(mtmsg)})
        '''修改url地址'''
        _mturl = 'http://218.25.10.21:7000/lf/201_new.asp?phone=%(phone)s&msgcontent=%(mtmsg)s&serviceup=%(serviceup)s&linkid=%(linkid)s&ext=%(ext)s'
        mturl = _mturl % kwargs
        starttime=time.time()
        d=getPage(mturl,timeout=5)
        d.addCallback(self.req_ok,mturl,starttime,mtstep_key)
        d.addErrback(self.req_failure,mturl,starttime,mtstep_key)
        return d

    def req_ok(self,result,mturl,starttime,):
        '''请求成功'''
        endtime=time.time()
        result=result.strip()
        costtime=endtime-starttime
        _msg='%s,OK:%s||costtime=%s||%s\r\n'%(
            datetime.datetime.today(),
            mturl,
            costtime,
            result.strip()
        )
        mtlog.write(_msg)
    def req_failure(self,failure,mturl,starttime,mtstep_key):
        '''请求失败'''
        endtime=time.time()
        costtime=endtime-starttime
        _msg='%s,FAILURE:%s||costtime=%s||%s\r\n'%(
            datetime.datetime.today(),
            mturl,
            costtime,
            failure.getErrorMessage(),
        )
        mtlog.write(_msg)
        print failure