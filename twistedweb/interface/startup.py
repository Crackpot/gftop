#coding=utf-8
from twisted.web import server
from urls import root
site=server.Site(root)
from twisted.application import service,strports
application=service.Application('web')
s=strports.service('tcp:9999',site)
s.setServiceParent(application)