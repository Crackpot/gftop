#coding=utf-8
"""
    文件的扩展名.rpy是python脚本，如果放在一个TwistedWeb服务目录，通过网络访问的时候，它将被执行。
    一个.rpy脚本必须定义一个变量， resource ，这是将渲染这一请求的资源对象。 
    .rpy文件是非常方便的快速发展和原型。因此在.rpy中定义了的资源子类将在每个web请求的时候被执行，当改变这个类的时候只要刷新页面就能看到它的改变。
"""
from twisted.web.resource import Resource
class MyResource(Resource):
    def render_GET(self,request):
        return "<html>Hello,crackpot!This is RpyScript</html>"
resource=MyResource
