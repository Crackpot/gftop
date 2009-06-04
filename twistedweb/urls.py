#coding=utf-8
from twisted.web import resource
from request import helloworld

class Toplevel(resource.Resource):
    def getChild(self,name,request):
        if name=='':
            return self
        return resource.Resource.getChild(self,name,request)
    def render(self,request):
        return 'ok@index'

class Monitor(resource.Resource):
    isLeaf=True
    def render(self,request):
        return 'ok@monitor'
    
class HelloworldIndex(resource.Resource):
    isLeaf=False
    def getChild(self,name,request):
        if name=='':
            return self
        return resource.Resource.getChild(self,name,request)
    def render(self,request):
        return 'ok@helloworld'
hw_url=HelloworldIndex()
hw_url.putChild('display',helloworld.Display())

root=Toplevel()
root.putChild('monitor',Monitor())
root.putChild('helloworld',hw_url)
