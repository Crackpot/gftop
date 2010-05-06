#coding=utf-8
r=range(0,9,2)
l=list(r);print l
t=tuple(r);print t
s=str(l)+str(t);print s
string='中华人民共和国万岁！';print string,len(string)
us=unicode(string);print us,len(us)
es=us.encode('utf-8');print es,len(es)
print max(r)
print min(r)
reversed(string)
li=[3,4,2,1,0,4,9,]
print sorted(li)
z=zip(li)
print z
for item in z:
    print item
    for v in item:
        print v