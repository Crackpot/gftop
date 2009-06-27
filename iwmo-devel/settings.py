# -*- coding: utf-8 -*-
import memcache, re, os, bsddb

#IWPROXY
IWPROXY_HOST = "127.0.0.1"  #211.157.110.22
IWPROXY_PORT = 11000


mc = memcache.Client(['127.0.0.1:11211'])
mdbc = memcache.Client(['59.60.30.243:21211'])

numre = re.compile(r'^\d+$')
phonere = re.compile(r'^1[3|5|8]\d{9}$')

#phone reglex expression
mobilere = re.compile(r'^(134|135|136|137|138|139|150|151|152|157|158|159|187|188)\d{8}$')
unionre = re.compile(r'^(130|131|132|155|156|185|186)\d{8}$')
telcomre = re.compile(r'^(133|153|180|189)\d{8}$')

extra_re = re.compile(r'^[a-zA-Z0-9\-\_\.]*$') #support a-zA-Z0-9-_.

PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
LOGPATH = os.path.join(PROJECT_PATH, 'log')
if not os.path.exists(LOGPATH):
    os.makedirs(LOGPATH, 0777)

