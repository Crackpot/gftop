#coding=utf-8
'''
http://www.pythonchallenge.com/pc/def/equality.html
'''
import re

data=open('Level03.txt').read()
print data
print '##############################################'
print "".join(re.findall("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+", data))  