#coding=utf-8
try:
    filename=raw_input('请输入文件名：')
    myfile=open(filename,'r')
    for eachline in myfile:
        print eachline
        #myfile.close()
except IOError,e:
    print '文件打开错误！'

