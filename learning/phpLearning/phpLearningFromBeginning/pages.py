#coding=utf-8

myfile = open('index.html','r')
reader = myfile.readlines()
for row in reader:
    #print row
    line = "<tr><td><a href=\"./"+row+"\">"+row+"</a></td></tr>"
    print line


