#coding=utf-8
from twisted.web import resource,server
from twisted.web.client import getPage
import sys
sys.path.append('/home/workspace/gftop/twistedweb')
import settings
from utils import render_to_response
from twisted.python import logfile

log=logfile.LogFile('sm.req.success.log',settings.LOGPATH,defaultMode=0777)
faillog=logfile.LogFile('sm.req.failure.log',settings.LOGPATH,defaultMode=0777)

class Request(resource.Resource):
    def render_POST(self,request):
        username=request.args.get('username',['username'])[0]
        birthday=request.args.get('birthday',['birthday'])[0]
        #return 'username=%s\ttypeOfUsername=%s\nbirthday=%s\ttypeOfBirthday=%s'%(self.username,type(self.username),self.birthday,type(self.birthday))
        if 1:
            rargs={
                'username':username,
                'birthday':birthday
            }
            requrl='http://interface.crackpot.com/sm?username=%s&birthday=%s'
            sendurl=requrl%(
                username,
                birthday,
            )
            d=getPage(sendurl,timeout=5)
            #d.addCallback(self.req_ok,request,sendurl,rargs)
            #d.addErrback(self.req_failure,request,sendurl,rargs)
            return server.NOT_DONE_YET
        else:
            txt='错误'
        return txt
    def req_ok(self,result,request,requrl,rargs):
        print result
        
        ret = result.strip()
        msg = '%s::%s,%s\n' % (
               datetime.datetime.today(),
               requrl,
               ret,
        )
        log.write(msg)
    
        msg, ln = ret.split('_')
    
        if msg != 'false':
            rargs.update({'msg': msg, 'ln':ln, })
            returl = 'http://localhost:8090/hello/display?username=%s&birthday=%s' % rargs
            request.redirect(returl)
        else:
            request.write(ret)
        request.finish()
        
    def req_failure(self,failure,request,requrl,rargs):
        print failure
        msg = '%s::%s,%s\n' % (
               datetime.datetime.today(),
               requrl,
               str(failure)
        )
        faillog.write(msg)
    
        request.write('false_NETGATERROR:%s' % str(failure))
        request.finish()