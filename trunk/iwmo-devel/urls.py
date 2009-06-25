#coding=utf-8
from twisted.web import http,resource

################################
from recvmo import *
from crackpot.urls import url_crackpot
class Recvmo(resource.Resource):
    '''点播网关接收mt地址'''
    isLeaf=False
    def getChild(self,name,request):
        if name=='':
            return self
        return resource.Resource.getChild(self, name, request)
    def render(self,request):
        return 'ok@recvmo'
url_recvmo=Recvmo()
#url_recvmo.putChild('suanming',base_suanming.Receive)

#~~~~~~~ring~~~~~~~~
from recvmo.ring import urls
url_recvmo.putChild('ring', urls.ring_url)
######################################
from mdispatch import *
class MiddleDispatch(resource.Resource):
    '''同一模糊指令分发'''
    isLeaf=False
    def getChild(self,name,request):
        if name=='':
            return self
        return resource.Resource.getChild(self, name, request)
    def render(self,request):
        return 'ok@dispatch'
url_dispatch=MiddleDispatch()

#####################################
#from monitor import m2008
class Monitor(resource.Resource):
    isLeaf=False
    def getChild(self,name,request):
        if name=='':
            return self
        return resource.Resource.getChild(self, name, request)
    def render(self,request):
        return 'ok@monitor'
url_monitor=Monitor()

#############################

class Toplevel(resource.Resource):
    isLeaf=False
    def getChild(self,name,request):
        if name=='':
            return self
        return resource.Resource.getChild(self, name, request)
    def render(self,ctx):
        return 'ok'
root=Toplevel()
root.putChild('recvmo', url_recvmo)
root.putChild('dispatch', url_dispatch)
root.putChild('monitor', url_monitor)
root.putChild('crackpot', url_crackpot)