#! /usr/bin/env python
#coding=utf-8
#from request.mo import request_path
from twisted.web import http,resource
import bsddb
db=bsddb.btopen('times.db')
#db['crackpot']='haha'
from process import steps
class Qingqiu(resource.Resource):
    isLeaf=True
    def render(self,request):
        self.phone=request.args.get('phone',[''])[0]
        self.linkid=request.args.get('linkid',[''])[0]
        self.spnumber=request.args.get('spnumber',[''])[0]
        self.order = '1'
        if self.phone and self.linkid:
            mocount = db.get(self.phone, 0)
            mocount = int(mocount)  + 1
            stepsInstance=steps()
            processTip=getattr(stepsInstance,'step_%s'%(mocount), stepsInstance.step_6)
            result=processTip()
            result = result % {
                'msg': self.order,
                'phone': self.phone,
            }
            db[self.phone] = str(mocount)
#
#            try:
#                stepsInstance=steps()
#                time=int(db[self.phone])
#                if time<6:
#                    processTip=getattr(stepsInstance,'step_%s'%(time+1))
#
#                    result=processTip()
#                    db[self.phone]=str(time+1)
#                else:
#                    result='您已经完成了六项操作，请勿重新提交！'
#
#            except Exception,e:
#                result=''
#                db[self.phone]='1'
#                time=db[self.phone]
            return '\
                phone:%s<br>\
                linkid:%s<br>\
                spnumber:%s<br>\
                time:%s<br>\
                result:%s'%(self.phone,self.linkid,self.spnumber,db[self.phone],result)
url_qingqiu=Qingqiu()

class Toplevel(resource.Resource):
    isLeaf=False
    def getChild(self,name,request):
        if name=='':
            return self
        return resource.Resource.getChild(self,name,request)
    def render(self,ctx):
        return 'ok@root<br>\
http://localhost:8000/request_path?phone=13767001234&linkid=1231231231&spnumber=13'
root=Toplevel()
root.putChild('request_path',url_qingqiu)