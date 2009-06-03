#coding=utf-8
"""
    Resource对象代表一个网站单一的URL段。在URL分析过程中， getChild在当前Resource产生的下一个Resource对象将被调用。 
    当达到叶资源时候，或者是因为没有更多的URL段或资源的isLeaf属性已设置为True ，通过调用render(request)来渲染叶资源 。
    在资源定位过程中，已经被处理和那些还没有得到处理的URL段在request.prepath和request.postpath中存在。 
    一个资源可以通过查看request.prepath的名单（网址段字符串）而知道它是在URL树的什么地方。 
    一个资源可以通过查看request.postpath知道哪些路径段将被处理。
    如果URL用斜线结尾，例如http://example.com/foo/bar/ ，最后的网址段将是一个空字符串。 资源从而知道他们的请求有或没有最后的斜线。 
"""
from twisted.web.resource import Resource
class Hello(Resource):
    isLeaf=True
    def getChild(self,name,request):
        if name=='':
            return self
        return Resource.getChild(self,name,request)
    def render_GET(self,request):
        return "Hello,world!I am located at %r."%(request.prepath,)

