#coding=utf-8
#author:crackpot

import urllib
def findFlag(source,flag):
    #index = tag[0][1].find("'")
    return source.find(flag)

    
def findNextPage(url): 
    for i in xrange(1):
        url
        data = urllib.urlopen(url).read()   #打开url读取数据
        data = unicode(data, 'gb2312').encode('utf-8')     #转换字符编码
        #print data
        flagNextPage='下一页'
        findFlag(data, flagNextPage)
        index_flagNextPage = data.find(flagNextPage)
        #print flagNextPage,"的位置：\t",findFlag(data, flagNextPage)
        flagPG='<div class="pg">'
        #print flagPG,"的位置：\t",
        slicePG=data[findFlag(data, flagPG):findFlag(data, flagNextPage)]
        #print "\nslicePG的内容为：\n",slicePG
        while '&nbsp;<a href=' in slicePG:      #取得下一页的地址
            slicePG='http://mp3.baidu.com/'+slicePG[findFlag(slicePG, '&nbsp;<a href=')+len('&nbsp;<a href='):findFlag(slicePG, '><font>下一页')]
        #print len(slicePG)
        #print slicePG
        return slicePG

url='http://mp3.baidu.com/m?f=3&rn=&tn=baidump3ring&ct=285212672&word=beyond&lm=-1&oq=beyon&rsp=0'      #Beyond
urls=[]
urls.append(url)

while 1:
    url=findNextPage(url)
    urls.append(url)
    print url
    if len(url)>=150:
        break
print len(urls)
#del urls[len(urls)-1]
print urls



    
    