#coding=utf-8
import csv

myfile=open('mobile_num_jixiong.db','r')
reader=csv.reader(myfile)
myfile.close
for row in reader:
    #print row        #无法显示中文
    #print type(row)    #list
    for item in row:
        print item
    #print len(row)
