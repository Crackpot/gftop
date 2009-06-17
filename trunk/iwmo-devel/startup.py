#! /usr/bin/env python
#coding=utf-8
from twisted.web import server
from urls import root
site=server.Site(root)
from twisted.application import service,strports
application=service.Application('zmsms')
s=strports.service('tcp:8000',site)
s.setServiceParent(application)
