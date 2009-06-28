# -*- coding: utf-8 -*-
"""
考考你流程,流程9步
"""

#mt1 = '恭喜,闯关成功!专业大师为您设计的《%(name)s》艺术签名,回复%(cmd)s确认下载\n\n询059187521000'
#mt2 = '姓名已开始设计,请回复数字选择签名字体\n%(cmd)s1,明星艺术签\n%(cmd)s2,商务公文签\n\n询0591875210001元/条'
#mt3 = '好的签名应符合本人的形象气质,请根据您的形象气质选择风格(回复数字)\n%(cmd)s1,刚劲有力\n%(cmd)s2,飘逸洒脱\n1元/条'
#mt4 = '请回复数字选择你想要的签名排版\n%(cmd)s1横排\n%(cmd)s2竖排\n\n询059187521000'
#mt5 = '最后一步,为便于签名接收请确认手机屏幕大小,回复数字选择\n%(cmd)s1较大\n%(cmd)s2中等\n\n1元/条!'
#mt6 = '点击下载:http://wap.9189.com/sign?phone=%(phone)s'

from utils import proxycache
from twisted.internet import defer
import tk as kaokaonitk
import datetime
from twisted.python import failure

class MT9Mixin(object):
    def __init__(self, phone="", step=0, cmd="", o2="-1"):
        """
        qs:该流程步骤用户答题编号
        preqs: 用户上一次答题编号
        preqs 与self.o2 进行比对判断是否回答正确.
        
        """
        self.phone = phone
        self.step = step
        self.cmd = cmd
        self.o2 = o2
        self.errnu = 0
        
        
        qs_step=step
        if self.step>11:
            qs_step = 11
            
        pre_qs = self.phone[(qs_step-1)-1]
        current_qs = self.phone[qs_step-1]
        
        self.qs = str((int(current_qs)%2) + 1)
        self.preqs = str((int(pre_qs)%2) + 1)
        
    def render(self):
        """调用MT模板"""
        mt_method = getattr(self, 'mt_%s' % self.step, self.mterrfull)
        mt_defer = mt_method()
        
        return mt_defer

    def mt_1(self):
        mt = "您赢取奖品后希望以何种方式发放(回复数字):%(cmd)s1实物奖品;%(cmd)s2对换现金(需扣除20％佣金)"
        msg = mt % {'cmd': self.cmd, }
        
        return defer.succeed(msg)
    
    def mt_2(self):
        if self.o2 == '2':
            jptype = '对换成现金'
        else:
            jptype = '实物奖品'
    
        mt = '您选择了%(jp_type)s,请回复数字%(cmd)s确认奖品发放为本手机联系'
        msg = mt % {'cmd': self.cmd, 'jp_type': jptype }
        
        return defer.succeed(msg)
    
    def mt_3(self):
        mt = '我们已登记您的资料,回复%(cmd)s开始赢取你的奖品,能抽到这么好的奖品用户不多,要加油哦!'
        msg = mt % {'cmd': self.cmd }
        
        return defer.succeed(msg)
    
    def mt_4(self):
        mt = '本期大奖诺基亚N95,数量有限,考考你,回答正确本题才有机会获奖:%(qs)s'
        question = kaokaonitk.cg1.get(self.qs)
        question = question % {'cmd': self.cmd, }
        msg = mt % {'qs': question }
        
        return defer.succeed(msg)
    
    def mt_5(self):
        print 'preqs=%s&qs=%s&o2=%s' % (self.preqs, self.qs, self.o2)
    
        if self.o2 == self.preqs and self.errnu<3:
            mt = '恭喜您答对!%(qs)s'
            question = kaokaonitk.cg2.get(self.qs)
            question = question % {'cmd': self.cmd, }
    
            msg = mt % {'qs': question }
            return defer.succeed(msg)
        else:
            
            mterror_defer= self.mterror1()
            return mterror_defer
        
    def mt_6(self):
        if self.o2 == self.preqs and self.errnu<3:
            mt = '恭喜再次答对,加油!第三题:%(qs)s'
            question = kaokaonitk.cg3.get(self.qs)
            question = question % {'cmd': self.cmd, }
    
            msg = mt % {'qs': question }
            return defer.succeed(msg)
        else:
            
            mterror_defer= self.mterror1()
            return mterror_defer
    
    def mt_7(self):
        if self.o2 == self.preqs and self.errnu<3:
            mt = '真厉害!最后2题了,加油!%(qs)s'
    
            question = kaokaonitk.cg4.get(self.qs)
            question = question % {'cmd': self.cmd, }
    
            msg = mt % {'qs': question }
            return defer.succeed(msg)
        else:
            
            mterror_defer= self.mterror1()
            return mterror_defer
    
    def mt_8(self):
        if self.o2 == self.preqs and self.errnu<3:
            mt = '非常棒!最后一题啦!%(qs)s'
    
            question = kaokaonitk.cg5.get(self.qs)
            question = question % {'cmd': self.cmd, }
    
            msg = mt % {'qs': question }
            
            return defer.succeed(msg)
        else:
            
            mterror_defer= self.mterror1()
            return mterror_defer
    
    def mt_9(self):
        if self.o2 == self.preqs and self.errnu<3:
            mt = '恭喜闯关成功!我们会在每周二12点后公布中奖结果.如果您中奖我们将短信及电话通知您。'
            return defer.succeed(mt)
        else:
            mterror_defer= self.mterror1()
            return mterror_defer
    
    def mterror1(self):
        mt = "很遗憾,您回答错误,我们奖励您一次机会,请重新回复短信回答上一题!(请在3分钟回答)"
        return defer.fail(failure.DefaultException(mt))
#        return defer.fail(mt)
    
    def mterror3(self):
        mt = '很遗憾,回答错误,您本次闯关失败,请下期活动再次参与!\n2元/条'
        return mt
    
    def mterror2(self):
        mt = "很遗憾,您回答错误,我们奖励您一次机会,请重新回复短信回答上一题!(请在3分钟回答)"
        mt = mt % {'cmd': self.cmd, }
        return mt
    
    def mterrfull(self):
        mt = "对不起,本月您已参加过本活动,谢谢您的参与!请下月继续参加!"
        return defer.succeed( mt )
    
    
    def mt_notfound(self):
        msg = "抱歉，您回复的短信有误，请确认后回复正确的短信，谢谢。"
        
        return defer.succeed(msg)
    
    
    def getName(self):
        d = proxycache.pcache.perform('gpa', self.phone)
        return d
    
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
