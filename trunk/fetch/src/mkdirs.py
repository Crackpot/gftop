#coding=utf-8
import os
def mkdirs(path):
    '''
    建立多级目录
    例如
    mkdirs('/tmp/s/s/ss/dd')
    '''
    if os.path.exists(path):
        return 
 
    paths=path.split('/')
    p='';
    for i in range(0,len(paths)):
        p=p+ paths[i]+'/'
        print p
        if not os.path.exists(p):
            os.mkdir(p)
            
mkdirs(path=raw_input())