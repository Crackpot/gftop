# -*- coding: utf-8 -*-
'''
<tr>
  <td class="p3Item1Num"></td>
  <td class="p3Itme1Sname"><a href="javascript:prelisten('28109881')">Cheery Up China</a></td>
  <td class="p3Itme1banben">&nbsp;</td>
  <td class="p3Itme1star"><a href="javascript:srchkey('张杰')">张杰</a></td>
  <td></td>
  <td class="p3Itme1pop"><img src="http://image2.sina.com.cn/sms/mms/osix/star23.gif" border="0"/></td>
  <td class="p3Itme1down"><a href="javascript:prelisten('28109881')"><img src="http://image2.sina.com.cn/sms/images/sms_image/img/ico_01.gif" width="20" height="19" border="0"/></a></td>
  <td class="p3Itme1send"><a href="javascript:prelisten('28109881')"><img src="http://image2.sina.com.cn/sms/images/sms_image/img/ico_02.gif" width="20" height="19" border="0"/></a></td>
</tr>
'''
import re
from sgmllib import SGMLParser  #导入分析器
class SongParser(SGMLParser):   #歌曲分析器类
    def reset(self):    #重置操作
        SGMLParser.reset(self)
        self.songs = {} #创建一个字典储存歌曲
        self.cursong = ''   #当前的歌曲
        self.insong = False #找到了新歌
        self.newsong = False    
        self.name = ''
        
    def start_td(self, tag):    #从"td"标签位置开始
        #<tr>
            #<td class="p3Item1Num"></td>
            #<td class="p3Itme1Sname"><a href="javascript:prelisten('28108847')">K歌情人</a></td>
            #<td class="p3Itme1banben">&nbsp;</td>
            #<td class="p3Itme1star"><a href="javascript:srchkey('品冠,梁静茹')">品冠,梁静茹</a></td>
            #<td></td>
            #<td class="p3Itme1pop"><img src="http://image2.sina.com.cn/sms/mms/osix/star24.gif" border="0"/></td>
            #<td class="p3Itme1down"><a href="javascript:prelisten('28108847')"><img src="http://image2.sina.com.cn/sms/images/sms_image/img/ico_01.gif" width="20" height="19" border="0"/></a></td>
            #<td class="p3Itme1send"><a href="javascript:prelisten('28108847')"><img src="http://image2.sina.com.cn/sms/images/sms_image/img/ico_02.gif" width="20" height="19" border="0"/></a></td>
        #</tr>

        if tag:
            if tag[0]:                
                if tag[0][1] == 'p3Itme1Sname': #歌曲的ID
                    self.insong = True  #整个页面里发现了新的一首歌
                elif tag[0][1] == 'p3Itme1pop': #图片，在这里结束
                    self.insong = False
        
    def start_a(self, tag): #从a标签位置开始
        #页面源码中以这种格式存在<a href="javascript:prelisten('28108837')">
        if self.insong and 'prelisten' in tag[0][1]:    #找到新歌并且tag标签中有“prelisten“，（试听）
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

### http://image2.sina.com.cn/sms/sinarc/preview/28/28100/28100765.wma
import urllib
for i in xrange(149):
    url = 'http://bf.sina.com.cn/sinarc_php/ringlist.php?aid=1315&page=%s' % str(i) #去除字符串的首位字符
    data = urllib.urlopen(url).read()   #打开url读取数据
    data = unicode(data, 'gbk').encode('utf-8')     #转换字符编码
#    data = open('sina.txt').read()
    parser = SongParser()   #创建歌曲分析器对象
    parser.feed(data)   #

    songs = parser.songs    #歌曲分析器中的songs
    for k,v in songs.items():
        print k, '||'.join(v)
