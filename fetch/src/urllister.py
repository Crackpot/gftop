#!/usr/bin/env python
#coding=utf-8
from sgmllib import SGMLParser
class URLLister(SGMLParser):
    def reset(self):    #reset 由 SGMLParser 的 __init__ 方法来调用，也可以在创建一个分析器实例时手工来调用。所以如果您需要做初始化，在 reset 中去做，而不要在 __init__ 中做。这样当某人重用一个分析器实例时，可以正确地重新初始化。
        SGMLParser.reset(self)
        self.urls=[]
    
    def start_a(self,attrs):    #只要找到一个 <a> 标记，start_a 就会由 SGMLParser 进行调用。这个标记可以包含一个 href 属性，或者包含其它的属性，如 name 或 title。attrs 参数是一个 tuple 的 list，[(attribute, value), (attribute, value), ...]。或者它可以只是一个有效的 HTML 标记 <a> (尽管无用)，这时 attrs 将是个空 list。 
        href=[v for k,v in attrs if k=='href']  #我们可以通过一个简单的多变量 list 映射来查找这个 <a> 标记是否拥有一个 href 属性。 像 k=='href' 的字符串比较是区分大小写的，但是这里是安全的。因为 SGMLParser 会在创建 attrs 时将属性名转化为小写。 
        if href:
            self.urls.extend(href)
        
    