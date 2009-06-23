#coding=utf-8
'''
http://www.pythonchallenge.com/pc/def/linkedlist.php
'''
import urllib
import re

prefix = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
next = "12345"

while True:
    data = urllib.urlopen(prefix + next).read()
    print data
    if data == "Yes. Divide by two and keep going.":
        next = str(int(next) / 2)
    elif re.search("(?<=and the next nothing is )[0-9]*", data):       
        next = "".join(re.findall("(?<=and the next nothing is )[0-9]*", data))
    else:
        break    