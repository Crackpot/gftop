#coding=utf-8
from twisted.web import resource
from twisted.web.client import getPage
import datetime,urllib,time
import sys
sys.path.append('/home/workspace/gftop/twistedweb')
import settings
from utils import render_to_response
from twisted.python import logfile


log=logfile.LogFile('helloworld.req.success.log',settings.LOGPATH,defaultMode=0777)
faillog=logfile.LogFile('helloworld.req.failure.log',settings.LOGPATH,defaultMode=0777)

class Index(resource.Resource):
    isLeaf=True
    def render(self,request):
        username=request.args.get('username',['crackpot'])[0]
        return 'username=%s'%(username)
    
class Display(resource.Resource):
    isLeaf=True
    def render(self,request):
        self.username=request.args.get('username',['crackpot'])[0]
        self.birthday=request.args.get('birthday',['19000909'])[0]
        ISOTIMEFORMAT='%Y-%m-%d %X'
        self.now=time.strftime(ISOTIMEFORMAT,time.localtime())
        content=render_to_response('./helloworld/display.html',\
            now=self.now,\
            username=self.username,\
            birthday=self.birthday,\
        )
        return content
    
class Request(resource.Resource):
    isLeaf=True
    def render_POST(self,Request):
        phone=request.args.get('phone',['nophone'])[0]
        rargs={
            'phone':phone,
        }
        requrl='http://127.0.0.1:8090/hellorequest?phone=%s'
        sendurl=requrl%(
            phone,
        )
        d=getPage(sendurl,timeout=5)
        d.addCallback(self.req_ok,request,sendurl,rargs)
        d.addErrback(self.req_failure,request,sendurl,rargs)
        return server.NOT_DONE_YET

        pass