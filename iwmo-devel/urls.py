#! /usr/bin/env python
#coding=utf-8
#from request.mo import request_path
from twisted.web import http,resource
class Qingqiu(resource.Resource):
    isLeaf=True
    def render(self,request):
        self.phone=request.args.get('phone',[''])[0]
        self.linkid=request.args.get('linkid',[''])[0]
        self.spnumber=request.args.get('spnumber',[''])[0]
        if self.phone and self.linkid:
            return self.phone+self.linkid+self.spnumber    
url_qingqiu=Qingqiu()

class Toplevel(resource.Resource):
    isLeaf=False
    def getChild(self,name,request):
        if name=='':
            return self
        return resource.Resource.getChild(self,name,request)
    def render(self,ctx):
        return 'ok@root'
root=Toplevel()
root.putChild('request_path',url_qingqiu)