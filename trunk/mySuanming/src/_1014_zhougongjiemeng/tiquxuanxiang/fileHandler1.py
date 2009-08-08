#coding=utf-8
import csv

"""
"""


myfile=open('周公解梦分类（已排序）.csv','r')
myfileTmp=open('tmp','w')
reader=csv.reader(myfile)
for row in reader:      #文件中的每一行
    #print row
    count=0
    for item in row:        #每一行的各个项
        #print count, item
        count=count+1
        #print row[0],row[1]
    eachline='<option>'+row[1]+'</option>\n'        
    #eachline='        <option value="'+row[0]+row[1]+'">'+row[1]+'</option>\n'
    print eachline
    myfileTmp.write(eachline)
myfile.close()