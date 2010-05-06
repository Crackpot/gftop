#coding=utf-8
who='knights'
what='Ni!'
print 'We are the %s who say %s'%(who,((what+' ')*4))

for item in ['我','你','他']:
    print item
    
for eachNum in range(3):
    print eachNum
    
foo='I love China'
for c in foo:
    print c

for i in range(len(foo)):
    print foo[i],'(%d)'%i
    
#同时实现循环索引和元素
for i,ch in enumerate(foo):
    print ch,'(%d)'%i
    
#列表解析
squared=[x**2 for x in range(4)]        #可以在同一行中使用一个for循环将所有的值放到一个列表当中
for i in squared:
    print i

#元组解析
tupleNum=(x*3 for x in range(5))
for i in tupleNum:
    print i