#coding=utf-8
from twisted.web import resource

class Monitor(resource.Resource):
    isLeaf=True
    def render(self,request):
        return 'ok@monitor'

class TopLevle(resource.Resource):
    def getChild(self,name,request):
        if name=='':
            return self
        return resource.Resource.getChild(self,name,request)
    def render(self,request):
        return 'ok@index'

root=TopLevle()
root.putChild('monitor',Monitor())