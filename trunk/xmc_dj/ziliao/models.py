#coding=utf8
from django.db import models
from django.utils import timezone

class Ziliao(models.Model):
    xuhao = models.CharField('序号', max_length=40, blank=False) #序号
    mingcheng = models.CharField('名称', max_length=128, blank=False) #名称
    changjia = models.CharField('厂家', max_length=128, blank=False) #厂家
    shuliang = models.IntegerField('数量', blank=False) #数量
    fumian = models.CharField('幅面', max_length=20) #幅面
    cudangshijian = models.DateTimeField('存档时间', blank=False) #存档时间
    shiyongdidian = models.CharField('使用地点', max_length=20) #使用地点
    beizhu = models.TextField('备注', blank=True, null=True) #备注
    fengmian = models.ImageField('封面', upload_to='upload/ziliao/%Y/%m/%d', blank=True, null=True)
    
    def __unicode__(self):
        return self.mingcheng
    
    class Meta:
        verbose_name = '资料'
        verbose_name_plural = '资料'
        app_label = u"资料"
        db_table = 'ziliao_ziliao'

class Jieyue(models.Model):
    ziliao = models.ForeignKey(Ziliao, verbose_name='资料名称')
    amount = models.IntegerField('数目', blank=False)
    jieyueren = models.CharField('借阅人', max_length=128, blank=False)
    jiechuren = models.CharField('借出人', max_length=128, blank=False)
    yajin = models.IntegerField('押金', blank=False)
    jieyueshijian = models.DateTimeField('借阅时间', blank=False)
    guihuanshijian = models.DateTimeField('归还时间', blank=True, null=True)
    
    #判断是否已归还
    def yihuan(self):
        if self.guihuanshijian != None:
            return self.guihuanshijian >= timezone.now()
        else:
            return False
        
    yihuan.admin_order_field = 'guihuanshijian'
    yihuan.short_description = '已还'
    
    def __unicode__(self):
        return self.ziliao.mingcheng
    
    class Meta:
        verbose_name = '借阅'
        verbose_name_plural = '借阅'
        app_label = u"资料"
        db_table = 'ziliao_jieyue'