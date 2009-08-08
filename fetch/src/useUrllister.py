#!/usr/bin/env python
#coding=utf-8
import urllib,urllister
#url12530="http://www.12530.com/newweb/v3/v3_search/search_index/P9/P9Z1/P9Z1Y1/12530/_/_/P1/P1Z1/P1Z1Y1/_/_/_/_/1/%E5%B0%8F%E6%B2%88%E9%98%B3/v3.html"
usock=urllib.urlopen("http://diveintopython.org/")
parse=urllister.URLLister()
parse.feed(usock.read())    #调用定义在 SGMLParser 中的 feed 方法，将 HTML 内容放入分析器中。 [4]  这个方法接收一个字符串，这个字符串就是 usock.read() 所返回的。 
usock.close()   #像处理文件一样，一旦处理完毕，您应该 close 您的 URL 对象。 
parse.close()   #您也应该 close 您的分析器对象，但出于不同的原因。feed 方法不保证对传给它的全部 HTML 进行处理，它可能会对其进行缓冲处理，等待接收更多的内容。只要没有更多的内容，就应调用 close 来刷新缓冲区，并且强制所有内容被完全处理。 
for url in parse.urls:  #一旦分析器被 close，分析过程也就结束了。parser.urls 中包含了在 HTML 文档中所有的链接 URL。
    print url