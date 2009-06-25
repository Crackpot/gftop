#coding=utf-8
'''
    算命流程
'''
#mtfree = "您想测算的是《$mtname》吗？请直接回复数字12确认测算\n询057188166971,本条免费"   #免费MT
#mt1 = "欢迎使用《$proname》，请回复A确认您输入的信息正确无误，为您全面分析独家揭密。"
#mt2 = "信息已确认，系统正在分析，回复A查看结果（分析结果仅供参考，要自信努力能改变运势）。"
#mt3 = "您的姓名分析结果，对您的事业、爱情运势有不利的一面，回复A看看您的姓名终级解析。"
#mt4 = "最后一步，回复A立即下载全部的分析结果。"
#mt5 = "点击$url查看结果，或在网站上输入验证码：$checkcode查看。"
#mtonemore = ""      #二次营销MT

import sys
sys.path.append('/home/workspace/gftop/iwmo-devel')

from utils import proxycache
from twisted.internet import defer
import datetime
from twisted.python import failure
class MT(object):
    def __init__(self, phone = '', step = 0, cmd = '', proname = ''):
        self.phone = phone
        self.step = step
        self.cmd = cmd
        self.proname = proname
    def render(self):
        '''调用MT模板'''
        mt_method = getattr(self, 'mt_%s'%self.step, self.mterrfull)
        mt_defer = mt_method()
        return mt_defer
    def mt_free(self):
        mt = "您想测算的是《%(mtname)s》吗？请直接回复数字12确认测算\n询057188166971,本条免费 "
        msg=mt%{'mtname':mtname}
        return defer.succeed(msg)
    def mt_1(self):
        mt = "欢迎使用《%(proname)s》，请回复A确认您输入的信息正确无误，为您全面分析独家揭密。"
        msg = mt % {'proname': self.proname, }
        return defer.succeed(msg)
    def mt_2(self):
        mt = "信息已确认，系统正在分析，回复A查看结果（分析结果仅供参考，要自信努力能改变运势）。"
        msg = mt
        return defer.succeed(msg)
    def mt_3(self):
        mt = "您的姓名分析结果，对您的事业、爱情运势有不利的一面，回复A看看您的姓名终级解析。"
        return defer.succeed(msg)
    def mt_4(self):
        mt = "最后一步，回复A立即下载全部的分析结果。"
        return defer.succeed(msg)
    def mt_5(self):
        mt = "点击%(url)s查看结果，或在网站上输入验证码：%(checkcode)s查看。"
        msg=mt%{'url':url, 'checkcode':checkcode}
        return defer.succeed(msg)

    def mt_notfound(self):
        msg = "抱歉，您回复的短信有误，请确认后回复正确的短信，谢谢。"
        return defer.succeed(msg)
    def _gotResult(self, result, cmd):
        """查询姓名结果"""
        print result
        name = "undefined"
        lr = result.split("$")
        if len(lr) == 13:
            name = lr[7]
            return name
    def _gotError(self, failure, cmd):
        """查询姓名失败"""
        name="undefined"
        return name