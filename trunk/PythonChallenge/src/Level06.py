#coding=utf-8
'''
    http://www.pythonchallenge.com/pc/def/channel.html
'''
import urllib,zipfile,re
data=zipfile.ZipFile('Level06.zip','r')
print data.printdir()
print data.read('readme.txt')
next='90052'
comments=''
while True:
    content=data.read(next+'.txt')
    comments+=data.getinfo(next+'.txt').comment;
    print content
    next=''.join(re.findall('[0-9]*',content))
    if next=='':
        break
    print comments
    