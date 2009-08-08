#!/usr/bin/env python
#coding=utf-8

"""
    Author: crackpot
"""
import re
#import baidusong
from sgmllib import SGMLParser  #导入分析器
class SongParser(SGMLParser):   #歌曲分析器类
    def reset(self):    #重置操作
        SGMLParser.reset(self)
        self.songs = {} #创建一个字典储存歌曲
        self.locateDict={}
        self.cursong = ''   #当前的歌曲
        self.insong = False #找到了新歌
        self.newsong = False    
        self.name = ''
        
    def start_td(self, tag):    #从"td"标签位置开始
        #<TR>
            #<TD width="10" align="left" class="tdline28">1</TD>
            #<TD class="tdline28 p14"><a href="http://mp3.baidu.com/tring?url=http%3A%2F%2Fmy%2E12530%2Ecom%2Fnewchannel%2Forder%2F600902000006283837%2F1%2F2703%2F2703%5Fzlss%2F%2D%2F%2D%2F%2D%2Forder%2Ehtm&sn=1&title=%D0%A1%C9%F2%D1%F4+%2D+%D0%A1%C9%F2%D1%F4%BD%CC%D1%B5%C8%CB" target="_blank" onclick="return or(event,this);"><font color="#c60a00">小沈阳</font> - <font color="#c60a00">小沈阳</font>教训人</a></TD>
            #<TD class="tdline28"><a href="http://mp3.baidu.com/tring?url=http%3A%2F%2Fmy%2E12530%2Ecom%2Fnewchannel%2Forder%2F600902000006283837%2F1%2F2703%2F2703%5Fzlss%2F%2D%2F%2D%2F%2D%2Forder%2Ehtm&sn=1&title=%D0%A1%C9%F2%D1%F4+%2D+%D0%A1%C9%F2%D1%F4%BD%CC%D1%B5%C8%CB" target=_blank onclick="return or(event,this);">铃声下载</a></TD>
            #<TD align=left class="tdline28"><img src="http://img.baidu.com/img/mp3/d8.gif" border=0></TD>
        #</TR>

        if tag:
            if tag[0]:                
                if tag[0][1] == 'tdline28 p14': #歌曲名称
                    self.insong = True  #整个页面里发现了新的一首歌
                elif tag[0][1] == 'tdline28': #铃声下载
                    self.insong = False
        
    def start_a(self, tag): #从a标签位置开始
        #页面源码中以这种格式存在<a href="javascript:prelisten('28108837')">
        if self.insong :#and 'tdline28 p14' in tag[0][1]:    #找到新歌并且tag标签中有“prelisten“，（试听）
            index = tag[0][1].find("'") #找到单引号标志，把它的位置赋值给index
            end = tag[0][1].find("'", index+1)  #找到第二个单引号标志，它的位置加1为结束地址
            music_id = tag[0][1][index+1:end]   #歌曲的ID就是单引号之间的数字，存储的属性为列表
            
            self.songs[music_id] = []   #songs是一个字典 songs={'28109752':'……'}，键名＝键值
            self.cursong = music_id     #cursong是一个字符串，其中保存歌曲的ID
        
        
    def handle_data(self, text):    #处理数据
        txt = text.strip()  #去掉text的空格
        if txt and self.insong: #txt不为空，找到了新歌
            self.songs[self.cursong].append(txt)
            #print txt            
        if txt == '':
            return


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
    
    
    
import urllib
songDict={}    #歌曲名：原始url地址
def searchRing(url):
    print '正在搜索铃声……'
    for i in xrange(1):
        urls=[]
        urls.append(url)

        while 1:    #把所有的有效页面地址都统计出来放到列表中
            url=findNextPage(url)
            urls.append(url)
            if len(url)>=150:
                break
            #print len(urls)
            del urls[len(urls)-1]
            #print urls
    
        for url in urls:    
            try:
                data = urllib.urlopen(url).read()   #打开url读取数据
            except Exception, e:
                #print url, e
                continue
            data = unicode(data, 'gb2312').encode('utf-8')     #转换字符编码
            parser = SongParser()   #创建歌曲分析器对象
            parser.feed(data)   
            songs = parser.songs    #歌曲分析器中的songs
            locateDict=parser.locateDict
            for k, v in songs.items():
                #print k,v
                #print  ''.join(v)
                for i in xrange(1):
                    url = k
                    data = urllib.urlopen(url).read()   #打开url读取数据
                    first_pos = '<param name="URL" value="'
                    findex = data.find(first_pos)
                    kindex = len(first_pos)
                    s_pos = '"'
                    sindex = data.find(s_pos, findex + kindex)
                    songURL = data[findex + kindex: sindex]
                    """
                        这里设置铃声名称的限制，下载beyond时，名称前7位为‘beyond-’
                        如果不要限制，可修改下面的if语句
                    """
                    if ((songURL != 'null')and(''.join(v)[:7] == 'beyond-')) :      #歌曲名称开头为“beyond-.“，并且URL非空                        
                        songDict[''.join(v)] = songURL
                        print ''.join(v), songURL
                        #print ''.join(songURL)
                        #print songDict
#    for k,v in songDict.items():
#        print k,v
    print '共找到%d首铃声'%len(songDict)
    #print songDict
    




#自动下载功能
import os, time, random

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

def downThemAll(path):
    #探测，文件不存在就创建，文件存在就清除内容
    myfile=open('baiduRings.csv','w')
    myfile.write('\n')
    myfile.close()
    count=1        
    for k,v in songDict.items():
        #songName=k
        singer=k[:k.find('-')]
        songName=k[(k.find('- ')+2):]
        print songName
        songUrl=v
        
         
        
        #文件扩展名
        ext = songUrl[(len(songUrl)-3):]
        #时间戳
        timeStamp=str(int(time.time()))
        #4位随机数
        randomSeed='%#04d' % random.randint(1,1000)
        #文件名
        fileName=path+timeStamp+randomSeed+'.'+ext
        print '\n下载第%d首铃声：'%count
        cmd='axel -o '+fileName+' '+songUrl
        try:
            os.system(cmd)
        except Exception,e:
            print '下载失败'
            continue
        count=count+1
        print '保存为%s'%fileName
        """
            将记录写入文件
        """
        print '写入记录……'
        myfile=open('baiduRings.csv','a')
        strFileInfo=singer+','+songName+','+songUrl+','+fileName+'\n'

        myfile.write(strFileInfo)
    print '文件写入完成！'
    myfile.close()
    print '\n下载任务完成！'
    
       
def checkPower(path):
    #留着接口，有机会完善
    """
        # Checking Files: Python supports several methods of checking if a file exists and checking its properties:

        * bool os.access(string path, int mode): returns TRUE if the filename exists and matches the mode query. The mode query can be any of the following constants:
          o os.F_OK: test the existence of path
          o os.R_OK: tests if path exists and is readable
          o os.W_OK: tests if path exists and is writable
          o os.X_OK: tests if path exists and is executable 


    """
    pass
    

#检查是否要下载
def flagDownThemAllCheck():
    flagDownThemAll=str(raw_input('是否下载全部文件？请输入y或n:'))
    if flagDownThemAll=='y':
        global path
        path=raw_input('请输入要保存文件的位置，请确保它存在(例：/home/crackpot/Desktop/rings/)\n如果您对此路径没有存取权限，本程序会退出。建议检查权限问题并重新运行此程序！\n')
        """
            这里检查路径
        """
        if os.path.exists(path):
            #print path
            checkPower(path)
            #当前日期
            today=time.strftime('%Y%m%d')
            path=path+today+'/'
            mkdirs(path)
        else:
            print '您输入的路径无效，请重新输入！'
        
        searchRing(url)
        downThemAll(path)
    elif flagDownThemAll=='n':
        print '您选择不下载文件！'
        flagSearchRingCheck()
    else:
        print '您的输入有误，请重新输入：'
        flagDownThemAllCheck()   


#检查是否要搜索
def flagSearchRingCheck():
    flagSearchRing=str(raw_input('是否搜索铃声？请输入y或n:'))
    if flagSearchRing=='y':
        searchRing(url)
    elif flagSearchRing=='n':
        print '您选择不搜索铃声，本次操作结束'
        #flagSearchRing()
    
print '此程序专门用户百度铃声的下载。尚有不完善之处，若在使用方面有任何疑问，请联系crackpot!'
global url
url=raw_input('请输入要下载铃声的首页面：\n')
#url='http://mp3.baidu.com/m?f=3&rn=&tn=baidump3ring&ct=285212672&word=beyond&lm=-1&oq=bey&rsp=0'
flagDownThemAllCheck()