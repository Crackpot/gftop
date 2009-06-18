#coding=utf-8
'''
    http://www.pythonchallenge.com/pc/def/ocr.html
'''
import string
class decoder(object):
    def __init__(self):
        self.myfile=open('Level02.txt')
        self.content=self.myfile.read()     #对比readlines,readline
    def printContent(self):
        print '%s\n%s\n%s'%(self.content,type(self.content),len(self.content))
    def decoder_1(self):
        #这是我的方法
        for i in self.content:
            if i in string.letters:
                print i,
instance=decoder()
instance.printContent()
instance.decoder_1()
