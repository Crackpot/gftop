#!/usr/bin/env python
#coding=utf-8

from apihelper import info
li=[]
info(li)

import odbchelper
info(odbchelper)
info(odbchelper, 30)
info(odbchelper, 30, 0)
info(odbchelper, collapse=0)
info(spacing=15, object=odbchelper)
