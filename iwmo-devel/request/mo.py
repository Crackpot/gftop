#coding=utf-8
from twisted.web import resource,server
from twisted.web.client import getPage
class request_path(resource.Resource):
    def render(self,request):
        self.phone=request.args.get('phone',[''])[0]
        self.linkid=request.args.get('linkid',[''])[0]
        self.spnumber=request.args.get('spnumber',[''])[0]
        if self.phone and self.linkid:
            return self.phone+self.linkid+self.spnumber
    def req_ok(self,result,requrl):
        return 'ok'
    def req_failure(self,failure,requrl):
        return 'false@dispatch'