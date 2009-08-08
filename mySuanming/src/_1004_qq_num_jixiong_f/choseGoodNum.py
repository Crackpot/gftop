#coding=utf-8
import csv,random

myfile=open('qq_num_jixiong.db','r')
reader=csv.reader(myfile)
global count
count=0
global dictXiangjie
dictXiangjie={}
global dictFenxi
dictFenxi={}
global listGood
listGood=[]
for row in reader:      #文件中的每一行
    #print row
    for item in row :       #每一行的各个元素
        #print count, item
        if count in range(5,15):
            dictXiangjie[item[:item.find('|')]]=item[item.find('|'):]
        elif count >15:
            dictFenxi[item[:item.find('|')]]=item[item.find('|'):]
        count+=1

print '详解'
for k,v in dictXiangjie.items():
    #print k,v
    pass
print '分析'
for k,v in dictFenxi.items():
    #print k,v
    if v[len(v)-5:]=='|吉|':
        print k,v
        listGood.append(v)
    pass


for num in random.randrange(11111,999999999,1):
    if num%80 in listGood:
        print num
myfile.close()