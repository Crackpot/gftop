#coding=utf-8
from twisted.web import resource
import send
import receive 
class CrackpotURL(resource.Resource):
    isLeaf=False
    def getChild(self,name,request):
        if name=='':
            return self
        return resource.Resource.getChild(self, name, request)
    def render(self,ctx):
        return 'ok@Crackpot'
url_crackpot=CrackpotURL()
url_crackpot.putChild('send', send.Send())
url_crackpot.putChild('receive',receive.Receive())