#coding=utf-8
import bsddb
class steps(object):
    def step_0(self):
        return 'o\n开始'
    def step_1(self):
        return '1\n直接回复%(msg)s确认下载您点播的艺术签名\n(不回复将作废)。'
    def step_2(self):
        return '2\n姓名已开始设计,请回复数字选择签名字体\n%(msg)s1,明星艺术签\n%(msg)s2,商务公文签'
    def step_3(self):
        return '3\n好的签名应符合本人的形象气质,请根据您的形象气质选择风格(回复数字)\n%(msg)s1,刚劲有力\n%(msg)s2,飘逸洒脱\n'
    def step_4(self):
        return '4\n请回复数字选择你想要的签名排版\n%(msg)s1横排\n%(msg)s2竖排'
    def step_5(self):
        return '5\n最后1步,为便于签名接收请确认手机屏幕大小,回复数字选择\n%(msg)s1较大\n%(msg)s2中等\n回复完本短信就能立刻收到签名啦!'
    def step_6(self):
        return '6\n点击下载:http://wap.9189.com/sign?phone=%(phone)s'
#instance=steps()
#i=1
#try:
#    db=bsddb.btopen('times.db')
#    #del db['test']
#    time=int(db['test'])
#    if  time<7:
#        func=getattr(instance,'step_%s'%time)
#        db['test']=str(time+1)
#        result=func()
#    else:
#        result=''
#except Exception,e:
#    print e
#    db['test']='1'
#print result

