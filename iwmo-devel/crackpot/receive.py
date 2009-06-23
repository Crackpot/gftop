#coding=utf-8
from twisted.web import resource
class Receive(resource.Resource):
    isLeaf=True
    def __init__(self):
        pass
    def render(self,request):
        self.username=request.args.get('username',['username'])[0]
        self.name=request.args.get('name',['name'])[0]
        self.age=request.args.get('age',['age'])[0]
        self.phone=request.args.get('phone',['phone'])[0]
        content='''
            用户名：%s<br>
            姓名：%s<br>
            年龄：%s<br>
            手机：%s<br>
        '''%(self.username,self.name,self.age,self.phone)
        return content
        