#coding=utf8
from danwei.models import Danwei
from django.db import models
from django.utils import timezone
from shebei.models import Shebei

class Ziliao(models.Model):
    zl_xuhao = models.CharField('序号', max_length=40, blank=False) #序号
    zl_mingcheng = models.CharField('名称', max_length=128, blank=False) #名称
    zl_changjia = models.CharField('厂家', max_length=128, blank=False) #厂家
    zl_shuliang = models.IntegerField('数量', blank=False) #数量
    zl_fumian = models.CharField('幅面', max_length=20) #幅面
    zl_cundangshijian = models.DateTimeField('存档时间',auto_now_add=True, blank=False) #存档时间
    zl_shiyongdidian = models.ForeignKey(Danwei, verbose_name='使用地点')
    zl_duiyingshebei = models.ForeignKey(Shebei, verbose_name='对应设备')
    zl_beizhu = models.TextField('备注', blank=True, null=True) #备注
    zl_fengmian = models.ImageField('封面', upload_to='upload/ziliao/%Y/%m/%d', blank=True, null=True)
    
    def __unicode__(self):
        return self.zl_mingcheng
    
#    class Meta:
#        app_label = u"资料"
#        verbose_name = '资料'
#        verbose_name_plural = '资料'
#        db_table = 'ziliao_ziliao'

class Jieyue(models.Model):
    jy_ziliao = models.ForeignKey(Ziliao, verbose_name='资料名称')
    jy_shumu = models.IntegerField('数目', blank=False)
    jy_jieyueren = models.CharField('借阅人', max_length=128, blank=False)
    jy_jiechuren = models.CharField('借出人', max_length=128, blank=False)
    jy_yajin = models.IntegerField('押金', blank=False)
    jy_jieyueshijian = models.DateTimeField('借阅时间', blank=False)
    jy_guihuanshijian = models.DateTimeField('归还时间', blank=True, null=True)
    
    #判断是否已归还
    def yihuan(self):
        if self.jy_guihuanshijian!= None:
            return self.jy_guihuanshijian >= timezone.now()
        else:
            return False
        
    yihuan.admin_order_field = 'jy_guihuanshijian'
    yihuan.short_description = '已还'
    
    def __unicode__(self):
        return self.jy_ziliao.zl_mingcheng
#    class Meta:
#        app_label = u"资料"
#        verbose_name = '借阅'
#        verbose_name_plural = '借阅'
#        app_label = u"资料"
#        db_table = 'ziliao_jieyue'
