#coding=utf-8
from twisted.web import resource
from twisted.web.client import getPage
from twisted.web import server
class Send(resource.Resource):
    isLeaf=True
    def displayContents(self,contents, request):
        request.write(contents)
        request.finish()
    def errorHandler(self,error, request):
        request.write("false")
        request.finish()        
    def render(self,request):
        self.username=request.args.get('username',['crackpot'])[0]
        self.name=request.args.get('name',['高飞'])[0]
        self.age=request.args.get('age',['23'])[0]
        self.phone=request.args.get('phone',['15979122400'])[0]
        #return 'ok@send'
        _sendurl='http://127.0.0.1:8000/crackpot/receive?username=%s&name=%s&age=%s&phone=%s'
        sendurl=_sendurl%(self.username,self.name,self.age,self.phone)
#        content='''
#            用户名：%s<br>
#            姓名：%s<br>
#            年龄：%s<br>
#            手机：%s<br>
#        '''%(self.username,self.name,self.age,self.phone)
        df=getPage(sendurl)
        df.addCallback(self.displayContents, request)
        df.addErrback(self.errorHandler, request)
        
        return server.NOT_DONE_YET
        
        #return content