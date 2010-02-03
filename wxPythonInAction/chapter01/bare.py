#! /usr/bin/env python
#coding=utf-8

# 导入必须的wxPython包
import wx

# 子类化wxPython应用程序类
class App(wx.App): # 引用wxPython的类、函数和常量
    # 定义一个应用程序的初始化方法
    def OnInit(self):
        frame = wx.Frame(parent = None, id = -1, title = 'Bare')
        frame.Show()
        return True

# 创建一个应用程序类的实例
app = App()
# 进入这个应用程序的主事件循环
app.MainLoop()
