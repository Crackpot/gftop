#coding=utf-8
import mkdirs
path=raw_input()
while 1:
    try:
        mkdirs(path)
    except Exception,e:
        print e
        continue