#coding=utf-8
from twisted.web import resource

class Index(resource.Resource):
    isLeaf=True
    def render(self,request):
        username=request.args.get('username',['username'])[0]
        birthday=request.args.get('birthday',['birthday'])[0]
        return '接口接收到的信息为：<br>username=%s<br>birthday=%s'%(username,birthday)
        pass