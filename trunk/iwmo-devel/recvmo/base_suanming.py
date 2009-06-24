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

currentmonth=datetime.datetime.today().month
log=logfile.DailyLogFile('suanming.mo.log',settings.LOGPATH,defaultMode=0777)
mtlog=logfile.DailyLogFile('suanming.mt.log',settings.LOGPATH,defaultMode=0777)

def getok(result):
    print result
def getfailure(failure):
    print failure
    
from utils import proxycache,common
#import re
#re_step=re.compile(r'^\d+$')
class Receive(resource.Resource):
    def __init__(self):
        self.nid=999        #通道编号
        self.pid=888        #产品编号
    def render(self,request):
        self.phone=request.args.get('phone',[None])[0]
        self.msg=request.args.get('msgcontent',[''])[0]
        self.linkid=request.args.get('linkid',[None])[0]
        self.serviceup=request.args.get('serviceup',['100'])[0]
        self.ext=request.args.get('ext',['7'])[0]
        
        _msg='%s: %s\r\n'%(
            datetime.datetime.today(),
            common.args2str(request.args)
        )
        log.write(_msg)
        
        self.cmd='802'  #发送的指令
        self.ln = '1062666777'  #用户上行号码
        self.cmd_length=len(self.cmd)
        
        self.o2='-1'    #用户的选择判断
        if len(self.msg)>self.cmd_length:       #发送短信的内容长度大于指令的长度
            self.o2=self.msg[self.cmd_length]
        if self.phone and self.linkid and self.msg and self.msg.startswith(self.cmd):
            mtstep_key='%s|%s'%(self.nid,self.phone)
            d=proxycache.pcache.perform('getmtstep',mtstep_key)
            d.addCallback(self._got_mtstep_ok)
            
