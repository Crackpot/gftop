#coding=utf-8
from twisted.web import server
import sys
sys.path.append('/home/workspace/gftop/iwmo-devel')
from urls import root
site=server.Site(root)

# Standard twisted application Boilerplate
from twisted.application import service,strports
application=service.Application('zmsms')
s=strports.service('tcp:8000',site)
s.setServiceParent(application)