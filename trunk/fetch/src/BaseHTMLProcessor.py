#!/usr/bin/env python
#coding=utf-8
"""
    SGMLParser 自身不会产生任何结果。它只是分析，分析，再分析，对于它找到的有趣的东西会调用相应的一个方法，但是这些方法什么都不做。SGMLParser 是一个 HTML 消费者 (consumer)：它接收 HTML，将其分解成小的、结构化的小块。正如您所看到的，在前一节中，您可以定义 SGMLParser 的子类，它可以捕捉特别标记和生成有用的东西，如一个网页中所有链接的一个列表。现在我们将沿着这条路更深一步。我们要定义一个可以捕捉 SGMLParser 所丢出来的所有东西的一个类，接着重建整个 HTML 文档。用技术术语来说，这个类将是一个 HTML 生产者 (producer)。
    BaseHTMLProcessor 子类化 SGMLParser，并且提供了全部的 8 个处理方法：unknown_starttag、unknown_endtag、handle_charref、handle_entityref、handle_comment、handle_pi、handle_decl 和 handle_data。 
    
"""
from sgmllib import SGMLParser

class BaseHTMLProcessor(SGMLParser):
    def reset(self):                        #1  reset 由 SGMLParser.__init__ 来调用。在调用父类方法之前将 self.pieces 初始化为空列表。self.pieces 是一个数据属性，将用来保存将要构造的 HTML 文档的片段。每个处理器方法都将重构 SGMLParser 所分析出来的 HTML，并且每个方法将生成的字符串追加到 self.pieces 之后。注意，self.pieces 是一个 list。也许您想将它定义为一个字符串，然后不停地将每个片段追加到它的后面。这样做是可以的，但是 Python 在处理 list 方面效率更高一些。 
        self.pieces = []
        SGMLParser.reset(self)

    def unknown_starttag(self, tag, attrs): #2  因为 BaseHTMLProcessor 没有为特别标记定义方法 (如在 URLLister 中的start_a 方法)， SGMLParser 将对每一个开始标记调用 unknown_starttag 方法。这个方法接收标记 (tag) 和属性的名字/值对的 list(attrs) 两参数，重新构造初始的 HTML，接着将结果追加到 self.pieces 后。 这里的字符串格式化有些陌生，我们将留到下一节再说明。 
        strattrs = "".join([' %s="%s"' % (key, value) for key, value in attrs])
        self.pieces.append("<%(tag)s%(strattrs)s>" % locals())

    def unknown_endtag(self, tag):          #3  重构结束标记要简单得多，只是使用标记名字，把它包在 </...> 括号中。 
        self.pieces.append("</%(tag)s>" % locals())

    def handle_charref(self, ref):          #4  当 SGMLParser 找到一个字符引用时，会用原始的引用来调用 handle_charref。如果 HTML 文档包含 &#160; 这个引用，ref 将为 160。重构原始的完整的字符引用只要将 ref 包装在 &#...; 字符中间。 
        self.pieces.append("&#%(ref)s;" % locals())

    def handle_entityref(self, ref):        #5  实体引用同字符引用相似，但是没有#号。重建原始的实体引用只要将 ref 包装在 &...; 字符串中间。(实际上，一位博学的读者曾经向我指出，除些之外还稍微有些复杂。仅有某种标准的 HTML 实体以一个分号结束；其它看上去差不多的实体并不如此。幸运的是，标准 HTML 实体集已经定义在 Python 的一个叫做 htmlentitydefs 的模块中了。从而引出额外的 if 语句。) 
        self.pieces.append("&%(ref)s" % locals())
        if htmlentitydefs.entitydefs.has_key(ref):
            self.pieces.append(";")

    def handle_data(self, text):            #6  文本块则简单地不经修改地追加到 self.pieces 后。 
        self.pieces.append(text)

    def handle_comment(self, text):         #7  HTML 注释包装在 <!--...--> 字符中。 
        self.pieces.append("<!--%(text)s-->" % locals())

    def handle_pi(self, text):              #8  处理指令包装在 <?...> 字符中。 
        self.pieces.append("<?%(text)s>" % locals())

    def handle_decl(self, text):
        self.pieces.append("<!%(text)s>" % locals())

    def output(self):               #1   这是在 BaseHTMLProcessor 中的一个方法，它永远不会被父类 SGMLParser 所调用。因为其它的处理器方法将它们重构的 HTML 保存在 self.pieces 中，这个函数需要将所有这些片段连接成一个字符串。正如前面提到的，Python 在处理列表方面非常出色，但对于字符串处理就逊色了。所以我们只有在某人确实需要它时才创建完整的字符串。 
            """Return processed HTML as a single string"""
            return "".join(self.pieces) #2     如果您愿意，也可以换成使用 string 模块的 join 方法：string.join(self.pieces, "")。 