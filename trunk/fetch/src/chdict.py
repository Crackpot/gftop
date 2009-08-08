#coding=utf-8
d={'beyond- 不再犹豫':'http://content.12530.com/cmsdata/batchmusic/20070724/kwd0VUPm.wma', 
   'beyond- 胡涂的人':'http://content.12530.com/newcmsdata/batchmusic/20080707/RyxLGs2N.wma'
}
output=''
for k,v in d.items():
    #print k,v  
    singer=k[:k.find('-')]
    songName=k[(k.find('- ')+2):]
    songUrl=v
#    print singer
#    print songName
#    print songUrl
    output=output+singer+','+songName+','+songUrl+'\n'
print output
myfile=open('file.txt','w')
myfile.write(output)
myfile.close()