#coding=utf-8
"""
    Site对象是负责建立HTTPChannel实例去解析HTTP请求，并开始查找进程。它们包含代表URL /的请求网站的根资源。
    网站对象作为一个端口和根资源对象之间侦听HTTP请求的胶水。 
    当使用twistd -n web --path /foo/bar/baz ，网站对象是创建提供文件的指定路径的根资源。 
"""
from twisted.web import server,resource
from twisted.internet import reactor

class Simple(resource.Resource):
    isLeaf=True
    def render_GET(self,request):
        return "<html>Hello,world!</html>"
site=server.Site(Simple())
reactor.listenTCP(8080,site)
reactor.run()