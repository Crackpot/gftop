#coding=utf8
from django.db import models

class Yuangong(models.Model):
    #基本资料
    xingming = models.CharField('姓名', max_length=20)
    xingbie = models.CharField('性别', choices=((u'男', '男'), (u'女', '女')), max_length=1)
    chushengnianyue = models.DateField('出生年月')
    shenfenzhenghao = models.CharField('身份证号', max_length=18)
    zhengzhimianmao = models.CharField('政治面貌', choices=((u'群众', '群众'), (u'团员', '团员') , (u'党员', '党员')), max_length=2)
    rudangtuanshijian = models.DateField('入党团时间', blank=True, null=True)
    jiguan = models.CharField('籍贯', max_length=15)
    zhuzhi = models.CharField('住址', max_length=50)
    lianxidianhua = models.CharField('联系电话', max_length=30)

    #工作信息
    cangongshijian = models.DateField('参工时间')
    baoxianhao = models.CharField('保险号', max_length=10)
    renshikahao = models.CharField('人事卡号', max_length=10)

    #文化
    wenhuachengdu = models.CharField('文化程度', choices=((u'小学', '小学'), (u'初中', '初中') , (u'中专', '中专'), (u'高中', '高中'), (u'大专', '大专') , (u'本科', '本科')), max_length=2)
    dyxl_yuanxiao = models.CharField('第一学历毕业院校', max_length=30)
    dyxl_zhuanye = models.CharField('专业', max_length=20, blank=True, null=True)
    dyxl_shangxueshijian = models.DateField('上学时间')
    hxxl_yuanxiao = models.CharField('后续学历毕业院校', max_length=30, blank=True)
    hxxl_zhuanye = models.CharField('后续学历专业', max_length=20, blank=True)
    hxxl_shangxueshijian = models.DateField('后续学历上学时间', blank=True, null=True)


    #danwei = models.ForeignKey(Danwei, verbose_name='单位')
    danwei = models.CharField('单位', choices=(
            (u'调度', '调度'), (u'服务', '服务'), (u'机电队', '机电队'), (u'技检', '技检'), (u'售煤', '售煤'), 
            (u'跳汰队', '跳汰队'), (u'洗水队', '洗水队'), (u'原煤队', '原煤队'), (u'职能', '职能'), (u'重介队', '重介队'),
            (u'装运队', '装运队'), 
    ), max_length=5)
    
    gongbie = models.CharField('工别', choices=(
            (u'固定工', '固定工'), (u'劳务工', '劳务工'), (u'全合工', '全合工')
    ), max_length=5)

    zhiwu = models.CharField('职务', choices=(
           (u'安监员', '安监员'), (u'安装工', '安装工'), (u'办事员', '办事员'), (u'采样', '采样'), (u'茶炉工', '茶炉工'),
           (u'厂长', '厂长'), (u'成本员', '成本员'), (u'电工', '电工'), (u'电焊工', '电焊工'), (u'调度员', '调度员'),
           (u'动力工', '动力工'), (u'队长', '队长'), (u'副队长', '副队长'), (u'干部', '干部'), (u'干事', '干事'),
           (u'工会干事', '工会干事'), (u'化验', '化验'), (u'机电安装工', '机电安装工'), (u'集控', '集控'), (u'技术员', '技术员'),
           (u'科员', '科员'), (u'库管员', '库管员'), (u'煤质采样', '煤质采样'), (u'门卫', '门卫'), (u'木工', '木工'),
           (u'女工干事', '女工干事'), (u'配电工', '配电工'), (u'皮带工', '皮带工'), (u'钳工', '钳工'), (u'售煤', '售煤'),
           (u'书记', '书记'), (u'司机', '司机'), (u'跳汰司机', '跳汰司机'), (u'铁工', '铁工'), (u'团总支书记', '团总支书记'),
           (u'推土机司机', '推土机司机'), (u'维护工', '维护工'), (u'武保', '武保'), (u'压风机司机', '压风机司机'), (u'杂工', '杂工'),
           (u'站长', '站长'), (u'职教干事', '职教干事'), (u'装车工', '装车工'), (u'总支干事', '总支干事'), (u'组长', '组长'), 
    ), max_length=6)
    

    jtcy_guanxi1 = models.CharField('家庭成员关系1', max_length=10, blank=True, null=True)
    jtcy_xingming1 = models.CharField('家庭成员姓名1', max_length=10, blank=True, null=True)
    jtcy_chushengnianyue1 = models.DateField('家庭成员出生年月1', blank=True, null=True)
    jtcy_lianxidianhua1 = models.CharField('家庭成员联系电话1', max_length=30, blank=True, null=True)
    jtcy_danwei1 = models.CharField('家庭成员单位1', max_length=10, blank=True, null=True)
    
    jtcy_guanxi2 = models.CharField('家庭成员关系2', max_length=10, blank=True, null=True)
    jtcy_xingming2 = models.CharField('家庭成员姓名2', max_length=10, blank=True, null=True)
    jtcy_chushengnianyue2 = models.DateField('家庭成员出生年月2', blank=True, null=True)
    jtcy_lianxidianhua2 = models.CharField('家庭成员联系电话2', max_length=30, blank=True, null=True)
    jtcy_danwei2 = models.CharField('家庭成员单位2', max_length=10, blank=True, null=True)

    jtcy_guanxi3 = models.CharField('家庭成员关系3', max_length=10, blank=True, null=True)
    jtcy_xingming3 = models.CharField('家庭成员姓名3', max_length=10, blank=True, null=True)
    jtcy_chushengnianyue3 = models.DateField('家庭成员出生年月3', blank=True, null=True)
    jtcy_lianxidianhua3 = models.CharField('家庭成员联系电话3', max_length=30, blank=True, null=True)
    jtcy_danwei3 = models.CharField('家庭成员单位3', max_length=10, blank=True, null=True)
    
    def __unicode__(self):
        return self.xingming

#    class Meta:
#        app_label = u"员工"
#        verbose_name = '员工'
#        verbose_name_plural = '员工'
#        db_table = 'yuangong_yuangong'
#        unique_together = (("xingming", "shenfenzhenghao"),)
