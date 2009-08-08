#coding=utf-8
class man:
    name='姓名'
    sex='性别'
    def qichuang(self):
        print '起床'
    def chifan(self):
        print '吃饭'
    def shuaya(self):
        print '刷牙'
    def shangxue(self):
        print self.name,'去上学'
        man.qichuang(self)
        man.chifan(self)
        man.shuaya(self)
xm=man()
xm.name='小明'
xm.sex='男'
print '姓名:%s\t性别:%s'%(xm.name,xm.sex)
xm.shangxue()