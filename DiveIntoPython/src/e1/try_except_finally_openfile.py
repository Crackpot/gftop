#coding=utf-8
try:
    filename=raw_input('请输入要读取的文件名:\n')
    f=open(filename,'r')
    for eachline in f:
        print eachline
    f.close()
except IOError,e:
    print '文件打开错误：\t%s'%e
finally:
    print '\n任务完成！'