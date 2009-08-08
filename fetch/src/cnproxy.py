#!/usr/bin/python
#coding=utf-8
#PYTHON
import re
import urllib
import urllib2
import sys


portnumind={"z":"3","m":"4","k":"2","l":"9","d":"0","x":"5","i":"7","w":"6","q":"8","b":"1"}

def getport(s):
    s = s.replace("+", "")
    rs = ""
    for c in list(s):
        rs += portnumind[c]
    return rs

i = 0
p = re.compile("<tr><td>(\d*.\d*.\d*.\d*)<SCRIPT type=text\/javascript>document.write\(\":\"([^)]*)\)<\/SCRIPT><\/td><td>(.*?)<\/td>")
for i in range(1, 10):
    webdata = urllib.urlopen("http://www.cnproxy.com/proxy" + str(i) + ".html").read()
    ms = p.finditer(webdata)
    for m in ms:
        #print m.group(1)+":"+getport(m.group(2))+"@"+m.group(3)
        sys.stdout.write(m.group(1))
        sys.stdout.write(":")
        sys.stdout.write(getport(m.group(2)))
        sys.stdout.write("@")
        sys.stdout.write(m.group(3))
        sys.stdout.write("\n")
        #print "\n"