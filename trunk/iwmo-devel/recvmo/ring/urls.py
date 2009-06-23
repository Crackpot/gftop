#coding=utf-8
from twisted.web import resource

#import ...
#############
class RingURL(resource.Resource):
    isLeaf=False
    def getChild(self,name,request):
        if name=='':
            return self
        return resource.Resource.getChild(self, name, request)
    def render(self,ctx):
        return 'ok@ring_mo'
ring_url=RingURL()