#coding=utf-8
from twisted.web import resource, server
from twisted.web.client import getPage
import datetime, urllib
import sys
sys.path.append('/home/workspace/gftop/iwmo-devel')
import settings
from twisted.python import logfile

log = logfile.LogFile('sm.req.success.log', settings.LOGPATH, defaultMode=0777)
faillog = logfile.LogFile('sm.req.failure.log', settings.LOGPATH, defaultMode=0777)

class resultDisplay(resource.Resource):
    def render(self,request):
        import cPickle as pickle
        import base64

        stn = request.args.get('stn', ['1001'])[0]
        sm_key_hexicode = request.args.get('sm_key_hexicode', ['None'])[0]
        sm_key_type = "pickle"

        url = 'http://211.160.78.112:9200/sm?stn=%s&sm_key_hexicode=%s&sm_key_type=%s'

        resulturl = url % (
                        stn,
                        sm_key_hexicode,
                        sm_key_type,
                    )

        c = getPage(resulturl, timeout=5)
        c.addCallback(self.reg_ok, request, resulturl)
        c.addErrback(self.reg_failure, request, resulturl)
        return server.NOT_DONE_YET

    def reg_ok(self,result,request,resulturl):
        ret = result.strip()
        content = '请求成功'
        request.write(content)
        request.finish()


    def reg_failure(self, failure,request,resulturl):
        print failure
        msg = '%s::%s,%s\n' % (
                datetime.datetime.today(),
                requrl,
                str(failure)
                )
        faillog.write(msg)

        request.write('false_NETGATERROR:%s' % str(failure))
        request.finish()


class Request(resource.Resource):

    def render_POST(self, request):
        import cPickle as pickle
        import base64

        phone = request.args.get('phone', ['nophone'])[0]

        mid = request.args.get('mid', [None])[0]
        channel = request.args.get('channel', '1')[0]
        pid = '16'
        fromurl = ''
        extra = request.args.get('extra', ['-1'])[0][0:200]
        rn = request.args.get('username', ['-1'])[0]
        stn = request.args.get('stn',['1001'])[0]
        ip = request.received_headers.get('remote_addr', '192.168.1.1')

        sm_key = '-1'
        parse_dispatch = getattr(self, 'parse_%s' % stn, self.parse_unkown)
        sm_key = parse_dispatch(request)

        sm_key_hexicode = urllib.quote(base64.b64encode(pickle.dumps(sm_key)))

        r1 = urllib.quote(sm_key)
        r2 = request.args.get('r2', ['-1'])[0]
        r3 = request.args.get('r3', ['-1'])[0]
        r4 = request.args.get('r4', ['-1'])[0]
        r5 = request.args.get('r5', ['-1'])[0]

        if  phone and settings.phonere.match(phone) and \
            mid and settings.numre.match(mid) and \
            rn and self.checkName(rn):
            rargs = {
                'phone': phone,
                'mid': mid,
                'channel': channel,
                'pid': pid,
                'extra': extra,
                'rn': rn,
                'r1': r1,
                'r2': r2,
                'r3': r3,
                'r4': r4,
                'r5': r5,
                'stn':stn,
                'sm_key_hexicode': sm_key_hexicode,
            }


            requrl = 'http://request.icpun.net:9011/suanming?phone=%s&mid=%s&channel=%s&extra=%s&rn=%s&r1=%s&r2=%s&r3=%s&r4=%s&r5=%s&stn=%s&ip=%s'

            sendurl = requrl % (
                phone,
                mid,
                channel,
                extra,
                urllib.quote(rn),
                urllib.quote(r1),
                r2,
                r3,
                r4,
                r5,
                stn,
                ip,
            )

            d = getPage(sendurl, timeout=5)
            d.addCallback(self.req_ok, request, sendurl, rargs)
            d.addErrback(self.req_failure, request, sendurl, rargs)
            return server.NOT_DONE_YET
        else:
            txt = '手机号码不正确'
        return txt

        smallclass = request.args.get('smallclass', ['nophone'])[0]
        return smallclass

    def checkName(self, name):
        '''判断姓名是否合法'''
        try:
            ret = unicode(name, 'utf-8')
            if len(ret)<0 or len(ret)>=6:
                return False
        except Exception, e:
            return False
        return True

    def req_ok(self, result, request, requrl, rargs):
        print result

        ret = result.strip()
        msg = '%s::%s,%s\n' % (
               datetime.datetime.today(),
               requrl,
               ret,
        )
        log.write(msg)

        msg, ln = ret.split('_')

        if msg != 'false':
            rargs.update({'msg': msg, 'ln':ln, })
            returl = '/p/sm/step2?phone=%(phone)s&mid=%(mid)s&channel=%(channel)s&extra=%(extra)s&msg=%(msg)s&ln=%(ln)s&stn=%(stn)s&sm_key_hexicode=%(sm_key_hexicode)s' % rargs
            request.redirect(returl)
        else:
            request.write(ret)
        request.finish()

    def req_failure(self, failure, request, requrl, rargs):
        print failure
        msg = '%s::%s,%s\n' % (
               datetime.datetime.today(),
               requrl,
               str(failure)
        )
        faillog.write(msg)

        request.write('false_NETGATERROR:%s' % str(failure))
        request.finish()

    def parse_1000(self, request):#称骨算命
            year = request.args.get('year',['None'])[0]
            month = request.args.get('month',['None'])[0]
            day = request.args.get('day',['None'])[0]
            hour = request.args.get('hour',['None'])[0]
            username = request.args.get('useranme',['None'])[0]

            ret = '|'.join( (year, month, day, hour) )
            return ret


    def parse_1001(self, request):#爱情魔法配,
        sex1 = request.args.get('sex1', ['None'])[0]
        sex2 = request.args.get('sex2',['None'])[0]
        sx1 = request.args.get('sx1', ['None'])[0]
        sx2 = request.args.get('sx2', ['None'])[0]
        ret = '|'.join( (sex1, sx1, sex2, sx2) )
        return ret

    def parse_1002(self, request):#手机号码吉凶
        mobelnum = request.args.get('phone',['None'])[0]
        return mobelnum

    def parse_1003(self, request):#情商密码
        myxz = request.args.get('myxz',['None'])[0]
        taxz = request.args.get('taxz',['None'])[0]

        ret = '|'.join( (myxz, taxz) )
        return ret

    def parse_1004(self, request):#qq号吉凶
        qq = request.args.get('qq', ['None'])[0]
        return qq


    def parse_1005(self, request):#三才吉凶
        name = request.args.get('username',['None'])[0]
        return name


    def parse_1006(self, request):#生日密码
        month = request.args.get('month',['None'])[0]
        day = request.args.get('day',['None'])[0]
        ret = '|'.join( (month, day) )
        return ret

    def parse_1007(self, request):#属相分析
        sx = request.args.get('sx',['None'])[0]
        return sx

    def parse_1017(self, request):#姓名分析
        xing = request.args.get('xingshi',['-1'])[0]
        ming = request.args.get('mingzi',['-1'])[0]
        ret = '|'.join( (xing,ming ) )
        return ret

    def parse_1009(self, request):#星座测算
        xz = request.args.get('xingzuo',['None'])[0]
        ret = xz
        return ret

    def parse_1010(self, request):#血型搭配爱情
        xue1 = request.args.get('xuexing1',['None'])[0]
        xue2 = request.args.get('xuexing2',['None'])[0]
        ret = '|'.join( (xue1,xue2) )
        return ret

    def parse_1011(self, request):#血型解析
        xue = request.args.get('xue',['None'])[0]
        ret = xue
        return ret


    def parse_1012(self, request):#智商分析
        xingzuo = request.args.get('xingzuo',['None'])[0]
        ret = xingzuo
        return ret

    def parse_1013(self, request):#指纹
        code = request.args.get('code', ['None'])[0]
        ret = code
        return ret

    def parse_1014(self, request):#周公解梦
        smallclass = request.args.get('smallclass',['None'])[0]
        ret = smallclass
        return ret

    def parse_1015(self, request):#鬼谷子
        year = request.args.get('year',['None'])[0]
        month = request.args.get('month',['None'])[0]
        day = request.args.get('day',['None'])[0]
        hour = request.args.get('jay',['None'])[0]
        username = request.args.get('useranme',['None'])[0]
        ret = '|'.join( (year, month, day, hour) )
        return ret

    def parse_1016(self, request):#八字桃花命书
           year = request.args.get('year',['None'])[0]
           month = request.args.get('month',['None'])[0]
           day = request.args.get('day',['None'])[0]
           username = request.args.get('useranme',['None'])[0]
           hour = request.args.get('hour',['None'])[0]
           ret = '|'.join( (year, month, day,hour) )
           return ret
    def parse_unkown(self, request):
        ret = '-1'
        return ret




