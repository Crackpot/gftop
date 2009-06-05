#coding=utf-8
from twisted.web import resource
from request import helloworld,sm

class HelloworldIndex(resource.Resource):
    '''Helloworld接口首页'''
    isLeaf=False
    def getChild(self,name,request):
        if name=='':
            return self
        return resource.Resource.getChild(self,name,request)
    def render(self,request):
        return 'ok@helloworld'
hw_url=HelloworldIndex()
hw_url.putChild('display',helloworld.Display())

class SmIndex(resource.Resource):
    '''算命接口首页'''
    isLeaf=False
    def getChild(self,name,request):
        if name=='':
            return self
        return resource.Resource.getChild(self,name,request)
    def render(self,request):
        return 'ok@sm'
sm_url=SmIndex()
sm_url.putChild('request',sm.Request())

class Monitor(resource.Resource):
    '''服务监控'''
    isLeaf=True
    def render(self,request):
        return 'ok@monitor'
    
class Toplevel(resource.Resource):
    def getChild(self,name,request):
        if name=='':
            return self
        return resource.Resource.getChild(self,name,request)
    def render(self,request):
        return 'ok@index'
    
root=Toplevel()
root.putChild('monitor',Monitor())
root.putChild('helloworld',hw_url)
root.putChild('sm',sm_url)