#coding=utf-8
s='I love China!'
#此种方法字符串最后一个字符不显示
for i in range(-1,-len(s),-1):  #第一个参数是起始索引，第二个是终止索引，第三个是步长
    print s[:i]
    
print s[:0],'什么都没有'

#此种方式能显示最后一个字符
for i in [None]+range(-1,-len(s),-1):
    print s[:i]