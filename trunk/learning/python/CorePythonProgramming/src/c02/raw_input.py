#coding=utf-8
user=raw_input('请输入您的用户名：')
print '您的用户名为：%s,其类型为：%s'%(user,type(user))
#下面输入数值字符串
num=raw_input('清输入一个数字：')
dnum=int(num)
print '您输入的数字为：%d,其类型为：%s'%(dnum,type(dnum))
help(raw_input)