#coding=utf-8
'''memcachedb接口'''
import datetime
from twisted.internet import defer
import settings
from twisted.python import logfile

log = logfile.LogFile('mdb.error.log', settings.LOGPATH, defaultMode=0777)
mdbsetlog = logfile.LogFile('mdb.set.log', settings.LOGPATH, defaultMode=0777)

def mdb_error(failure):
    msg = '%s::%s\n' % (datetime.datetime.today(), str(failure))
    log.write(msg)

def incrUsrStep(nid, phone):
    '''保存用户发送条数，返回结果'''
    key = 'mo_%s_%s' % (nid, phone)
    count = settings.mdbc.get(key)
    if not count:
        settings.mdbc.set(key, 1)
        count = 1
    else:
        settings.mdbc.incr(key, 1)
        count = count + 1

    return count

def decrUsrStep(nid, phone):
    '''保存用户发送条数，返回结果'''
    key = 'mo_%s_%s' % (nid, phone)
    count = settings.mdbc.get(key)
    if not count:
        settings.mdbc.set(key, 0)
        count = 0
    else:
        settings.mdbc.decr(key, 1)
        count = count - 1
    return count

def getUsrStep(nid, phone):
    key = 'mo_%s_%s' % (nid, phone)
    step = 0
    _step = settings.mdbc.get(key)
    if _step:
        step = _step
    return step

def resetUsrStep(nid, phone):
    '''保存用户发送条数，返回结果'''
    key = 'mo_%s_%s' % (nid, phone)
    settings.mdbc.set(key, 0)

def getPhoneName(phone):
    '''保存用户姓名

    key: '%s|name'
    value: '姓名', maxlength=4
    '''
    key = '%s|name' % phone
    name = settings.mdbc.get(key)
    if not name:
        name = '姓名'
    return name

def getPhoneRing(phone):
    '''保存用户姓名

    key: '%s|name'
    value: '姓名', maxlength=4
    '''
    key = '%s|name' % phone
    name = settings.mdbc.get(key)
    if not name:
        name = 'undefined'
    return name

def getRingUrl(phone):
    key = '%s|ringurl' % phone
    ring_url = settings.mdbc.get(key)

    if not ring_url:
        ring_url = 'http://dn.pzzz.org/ring/20090215/ha0273.mp3'

    print 'key=%s|url=%s' % (key, ring_url)

    return ring_url


def getErrnum(currentmonth, nid, phone):
    '''查询用户发送错误次数'''
    key = '%s_%s_%s_errnu' % (currentmonth, nid, phone)

    errnu = 0
    _errnu = settings.mdbc.get(key)
    if _errnu:
        errnu = int(_errnu)
    return errnu

def setErrnum(currentmonth, nid, phone):
    '''设置用户回答错误次数'''
    key = '%s_%s_%s_errnu' % (currentmonth, nid, phone)
    en = 0
    _currenten = settings.mdbc.get(key)
    if _currenten:
        settings.mdbc.incr(key, 1)
        en = _currenten + 1
    else:
        settings.mdbc.set(key, 1)
        en = 1

    msg = '%s:%s\n' % (key, str(en))
    mdbsetlog.write(msg)
    return en

def getKKNUsrPwd(phone):
    key = '%s_kkn_pwd' % phone
    pwd = '11111'
    _pwd = settings.mdbc.get(key)
    if _pwd:
        pwd = _pwd
    return pwd

def setKKNUsrPwd(phone, pwd):
    key = '%s_kkn_pwd' % phone
    settings.mdbc.set(key, pwd)

    msg = '%s:%s\n' % (key, pwd)
    mdbsetlog.write(msg)
    return pwd

def resetKKNUsrPwd():
    pass


def getPhoneDispatch(phone):
    '''根据手机号码匹配状态报告'''
    key = 'dispatch_%s' % phone
    dbvalue = settings.mdbc.get(key)
    pid, nid = ('-1', '-1')
    if dbvalue:
        tmp = dbvalue.split('_')
        if len(tmp) == 2:
            pid, nid = tmp

    return (pid, nid)

def savePhoneDispatch(result, phone, pid, nid):
    '''保存号码对应产品编号，网关编号'''
    key = 'dispatch_%s' % phone
    value = '%s_%s' % (pid, nid)
    settings.mdbc.set(key, value)
    return True

def s_dispatch(*args, **kwargs):
    return defer.succeed('ok').addCallback(savePhoneDispatch, *args, **kwargs).addErrback(mdb_error)


##############################################################
######################m3gp####################################
##############################################################
def getPhoneM3gp(phone):
    key = '%s|3gpurl' % phone
    url = settings.mdbc.get(key)
    if not url:
        url = 'http://211.99.199.85/content/upload/movie/200903271435426346.3gp'
#        url = 'http://211.99.199.85/content/upload/movie/200903191539139443.3gp'
    return url

def getFileName(phone, pid):
    '''保存
    key: '%(phone)s|%(pid)s|name'
    '''
    key = '%s|%s|name' % (phone, pid)
    name = settings.mdbc.get(key)
    if not name:
        name = '女子大乱斗'

    return name
