#coding=utf-8
from twisted.web import resource
import sm

class Toplevel(resource.Resource):
    def getChild(self,name,request):
        if name=='':
            return self
        return resource.Resource.getChild(self,name,request)
    def render(self,request):
        return 'ok@index'
    
root=Toplevel()
root.putChild('sm',sm.Index())
        
