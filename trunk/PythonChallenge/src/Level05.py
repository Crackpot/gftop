#coding=utf-8
'''
    http://www.pythonchallenge.com/pc/def/peak.html
'''
import sys,urllib,pickle
obj=pickle.load(urllib.urlopen('http://www.pythonchallenge.com/pc/def/banner.p'))
print obj
for tmp in obj:
    for value in tmp:
        sys.stdout.write(value[0]*value[1])
    print 