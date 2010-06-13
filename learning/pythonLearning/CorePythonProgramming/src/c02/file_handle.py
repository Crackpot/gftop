#coding=utf-8
import os
filename=raw_input('请输入文件名：')
if not os.path.exists(filename):
    print '您指定的文件不存在，正在建立'
    myfile=open(filename,'w')
else:
    dictMode={1:'r',2:'w',}
    mode=int(raw_input('请选择期望的文件操作：\n1-读；2-写\n'))
    mode=dictMode[mode]
    #print mode,type(mode)
    myfile=open(filename,mode)
    if mode=='r': #读操作
        print '显示文件全部内容：'
        for eachline in myfile.readlines():
            print eachline
    elif mode=='w':#写操作
        content=raw_input('请输入要向文件写入的内容:')
        myfile.write(content)
myfile.close()