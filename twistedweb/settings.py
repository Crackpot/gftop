#coding=utf-8
import os

PROJECT_PATH=os.path.dirname(os.path.abspath(__file__))
LOGPATH=os.path.join(PROJECT_PATH,'log')
if not os.path.exists(LOGPATH):
    os.makedirs(LOGPATH, 0777)
    
MAKO_TEMPLATE_DIRS=os.path.join(PROJECT_PATH,'templates')
