#coding=utf8
from danwei.models import Danwei
from django.db import models

class Wenjian(models.Model):
    wj_biaoti = models.CharField(max_length=128, verbose_name='文件标题')
    wj_fazi = models.ForeignKey(Danwei, verbose_name='发自', related_name='fazi_danwei')
    wj_fazhi = models.ManyToManyField(Danwei, verbose_name='发至', related_name='fazhi_danwei')
    wenjian = models.FileField(upload_to = 'uploads/wenjian')
    wj_scsj = models.DateTimeField('上传时间', auto_now_add=True)
    
    def __unicode__(self):
        return self.wj_biaoti
