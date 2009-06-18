#coding=utf-8
import string
'''
    http://www.pythonchallenge.com/pc/def/map.html
'''
codedmessage='''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. '''
def decode1():
    str=''
    for c in codedmessage:
        if c in string.letters:
            str+=chr((ord(c)+2-97)%26+97)
        else:
            str+=c
    print codedmessage
    print str
def decode2():
    o=""
    for x in codedmessage:
        if ord(x)>=ord('a') and ord(x)<=ord('z'):
            o+=chr((ord(x)+2-ord('a'))%26+ord('a'))
        else:
            o+=x
    print o
def decode3():
    table=string.maketrans(
        'abcdefghijklmnopqrstuvwxyz',
        'cdefghijklmnopqrstuvwxyzab'
    )
    print string.translate(codedmessage, table)
    print string.translate('map', table)
def decode4():
    table=string.maketrans(
        string.ascii_lowercase,
        string.ascii_lowercase[2:]+string.ascii_lowercase[:2]
    )
    print string.translate(codedmessage, table)
    print codedmessage.translate(table)
    print string.translate('map', table)
def decode5():
    import os
    os.system('curl http://www.pythonchallenge.com/pc/def/map.html | tr a-z c-za-b')
def decode6():
    print ''.join([chr(ord(x)+2)for x in 'map'])
def decode7():
    cypher=dict(zip(string.lowercase,string.lowercase[2:]+string.lowercase[:2]))
    print ''.join(cypher.get(c,c) for c in codedmessage)
decode1()
decode2()
decode3()
decode4()
decode5()
decode6()
decode7()