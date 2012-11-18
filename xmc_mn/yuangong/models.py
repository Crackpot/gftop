#coding=utf8
from django.db import models
from danwei.models import Danwei

class Xingbie(models.Model):
    xingbie = models.CharField(max_length=2, primary_key=True)

    def __unicode__(self):
        return self.xingbie

#    class Meta:
#        abstract = False
#        app_label = u"员工"
#        verbose_name = '性别'
#        verbose_name_plural = '性别'
#        db_table = 'yuangong_xingbie'

class Wenhuachengdu(models.Model):
    wenhuachengdu = models.CharField(max_length=10)

    def __unicode__(self):
        return self.wenhuachengdu

#    class Meta:
#        app_label = u"员工"
#        verbose_name = '文化程度'
#        verbose_name_plural = '文化程度'
#        db_table = 'yuangong_wenhuachengdu'

class Zhengzhimianmao(models.Model):
    zhengzhimianmao = models.CharField(max_length=6)
    def __unicode__(self):
        return self.zhengzhimianmao

#    class Meta:
#        app_label = u"员工"
#        verbose_name = '政治面貌'
#        verbose_name_plural = '政治面貌'
#        db_table = 'yuangong_zhengzhimianmao'


class Gongbie(models.Model):
    gongbie = models.CharField(max_length=10)
    def __unicode__(self):
        return self.gongbie

#    class Meta:
#        app_label = u"员工"
#        verbose_name = '工别'
#        verbose_name_plural = '工别'
#        db_table = 'yuangong_gongbie'


class Gongzhong(models.Model):
    gongzhong = models.CharField(max_length=10)
    def __unicode__(self):
        return self.gongzhong

#    class Meta:
#        app_label = u"员工"
#        verbose_name = '工种'
#        verbose_name_plural = '工种'
#        db_table = 'yuangong_gongzhong'


class Yuangong(models.Model):
    #基本资料
    xingming = models.CharField('姓名', max_length=20)
    xingbie = models.ForeignKey(Xingbie, verbose_name='性别')
    chushengnianyue = models.DateField('出生年月')
    shenfenzhenghao = models.CharField('身份证号', max_length=18)
    zhengzhimianmao = models.ForeignKey(Zhengzhimianmao, verbose_name='政治面貌')
    rudangtuanshijian = models.DateField('入党团时间', blank=True, null=True)
    jiguan = models.CharField('籍贯', max_length=15)
    zhuzhi = models.CharField('住址', max_length=50)
    lianxidianhua = models.CharField('联系电话', max_length=30)

    #工作信息
    cangongshijian = models.DateField('参工时间')
    baoxianhao = models.CharField('保险号', max_length=10)
    renshikahao = models.CharField('人事卡号', max_length=10)

    #文化
    wenhuachengdu = models.ForeignKey(Wenhuachengdu, verbose_name='文化程度')
    diyixueli_yuanxiao = models.CharField('第一学历毕业院校', max_length=30)
    diyixueli_zhuanye = models.CharField('专业', max_length=20)
    diyixueli_shangxueshijian = models.DateField('上学时间')
    houxuxueli_yuanxiao = models.CharField('后续学历毕业院校', max_length=30, blank=True)
    houxuxueli_zhuanye = models.CharField('后续学历专业', max_length=20, blank=True)
    houxuxueli_shangxueshijian = models.DateField('后续学历上学时间', blank=True, null=True)


    danwei = models.ForeignKey(Danwei, verbose_name='单位')
    gongbie = models.ForeignKey(Gongbie, verbose_name='工别')
    gongzhong = models.ForeignKey(Gongzhong, verbose_name='工种')

    jiatingchengyuan_guanxi1 = models.CharField('家庭成员关系1', max_length=10)
    jiatingchengyuan_xingming1 = models.CharField('家庭成员姓名1', max_length=10)
    jiatingchengyuan_chushengnianyue1 = models.DateField('家庭成员出生年月1')
    jiatingchengyuan_lianxidianhua1 = models.CharField('家庭成员联系电话1', max_length=30)
    jiatingchengyuan_danwei1 = models.CharField('家庭成员单位1', max_length=10)
#"家庭成员
#出生年月"    联系电话    工作单位

    def __unicode__(self):
        return self.xingming

#    class Meta:
#        app_label = u"员工"
#        verbose_name = '员工'
#        verbose_name_plural = '员工'
#        db_table = 'yuangong_yuangong'
#        unique_together = (("xingming", "shenfenzhenghao"),)
