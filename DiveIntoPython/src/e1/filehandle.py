#coding=utf-8
myfile=open('/tmp/tmp','w')     #生成输出文件
myfile.write("hello crackpot\n")
#myfile.close
input=open('/tmp/tmp','r') 
print input.readlines()
