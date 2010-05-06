#coding=utf-8
'''
http://www.pythonchallenge.com/pc/return/bull.html
http://www.pythonchallenge.com/pc/return/sequence.txt
a = [1, 11, 21, 1211, 111221, 
'''
count = 0
s = "1"
a = [s]     #数组a的第一个元素是1
while count < 31:       #要求出数组下标为30的元素长度
   j = 0    #每个元素的下标
   news = ""    #        #新产生的下一个元素
   while j < len(s):    #
       i = j    #下标
       while j < len(s) and s[i] == s[j]:   #每个元素其中的数字相同的话
           j += 1
       news += str(j-i) + s[i]
   a += [news]
   s = news
   count += 1
counta=0
for item in a:
    print '%s=>%s'%(counta,item)
    counta+=1
print 'a[30]的长度：',len(a[30])
