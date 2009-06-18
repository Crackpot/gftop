#! /usr/bin/env python
#coding=utf-8
from wxPython.wx import *
class MyApp(wxApp):
    def OnInit(self):
        frame=wxFrame(NULL,-1,"haha")
        frame.Show(True)
        self.SetTopWindow(frame)
        return True
app=MyApp(0)
app.MainLoop()