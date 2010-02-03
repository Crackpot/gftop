#! /usr/bin/env python
#coding=utf-8

# 导入必须的wxPython包
import wx

# 子类化wxPython应用程序类
class MyFrame(wx.Frame):
    # 定义一个应用程序的初始化方法
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "My Frame", size = (300,300))
        panel = wx.Panel(self, -1)
        panel.Bind(wx.EVT_MOTION, self.OnMove)
        wx.StaticText(panel, -1, "Pos:", pos=(10, 12))
        self.posCtrl = wx.TextCtrl(panel, -1, "", pos=(40, 10))
    def OnMove(self, event):
        pos = event.GetPosition()
        self.posCtrl.SetValue("%s, %s" % (pos.x, pos.y))

if __name__ == '__main__':
    # 创建一个应用程序类的实例
    app = wx.PySimpleApp()
    frame = MyFrame()
    frame.Show(True)
    # 进入这个应用程序的主事件循环
    app.MainLoop()
