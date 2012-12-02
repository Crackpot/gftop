#coding=utf8
from django.contrib import admin
from django.http import HttpResponse
from django.template import loader
from django.template.context import Context
from models import Yuangong, Zhiwu, Gongzhong

class GongzhongAdmin(admin.ModelAdmin):
    actions = ['export_csv']
    
    def export_csv(self, request, queryset):
        response = HttpResponse(mimetype='text/csv')
        response['Content-Disposition'] = 'attachment; filename=%s' % '工种.csv'
        t = loader.get_template('yuangong/csv.html')

        datadict = [('id','工种')]
    
        for o in queryset:
            datadict.append((o.id, o.gongzhong,))

        c = Context({
            'data': datadict,
        })
        result = t.render(c)
        result = result .encode('utf8')
        response.write(result)
        return response

class ZhiwuAdmin(admin.ModelAdmin):
    actions = ['export_csv']
    
    def export_csv(self, request, queryset):
        response = HttpResponse(mimetype='text/csv')
        response['Content-Disposition'] = 'attachment; filename=%s' % '职务.csv'
        t = loader.get_template('yuangong/csv.html')

        datadict = [('id','职务')]
    
        for o in queryset:
            datadict.append((o.id, o.zhiwu,))

        c = Context({
            'data': datadict,
        })
        result = t.render(c)
        result = result .encode('utf8')
        response.write(result)
        return response
    
class YuangongAdmin(admin.ModelAdmin):
    search_fields = ('xingming',)
    list_display = ('xingming', 'xingbie', 'danwei', 'chushengnianyue')
    
    actions = ['export_csv']
    
    def export_csv(self, request, queryset):
        response = HttpResponse(mimetype='text/csv')
        response['Content-Disposition'] = 'attachment; filename=%s' % '员工.csv'
        t = loader.get_template('yuangong/csv.html')

        datadict = [
            ('id', 'xingming', 'xingbie', 'chushengnianyue', 'cangongshijian', 'baoxianhao', 'renshikahao', 'shenfenzhenghao', 'zhuzhi', 'jiguan',
            'wenhuachengdu', ' dyxl_yuanxiao', ' dyxl_zhuanye', ' dyxl_shangxueshijian',
            'hxxl_yuanxiao', ' hxxl_zhuanye', ' hxxl_shangxueshijian', 
            'zhengzhimianmao', ' rudangtuanshijian', ' gongbie', ' gongzhong', ' zhiwu', ' danwei', ' lianxidianhua', 
            'jtcy_guanxi1', ' jtcy_xingming1', ' jtcy_chushengnianyue1', ' jtcy_lianxidianhua1', ' jtcy_danwei1', 
            'jtcy_guanxi2', ' jtcy_xingming2', ' jtcy_chushengnianyue2', ' jtcy_lianxidianhua2', ' jtcy_danwei2', 
            'jtcy_guanxi3', ' jtcy_xingming3', ' jtcy_chushengnianyue3', ' jtcy_lianxidianhua3', ' jtcy_danwei3',),
            ('id','姓名','性别','出生年月','参加工作时间', '劳动保险号','人事卡号', '身份证号', '详细住址', '籍贯',
            '文化程度','第一学历毕业院校','专业','上学时间',
            '后续学历毕业院校','后续学历专业','后续学历上学时间',
            '政治面貌', '入党团时间', '工别', '工种', '职务', '单位', '联系电话',
            '家庭成员关系1','家庭成员姓名1','家庭成员出生年月1','家庭成员联系电话1','家庭成员单位1',
            '家庭成员关系2','家庭成员姓名2','家庭成员出生年月2','家庭成员联系电话2','家庭成员单位2',
            '家庭成员关系3','家庭成员姓名3','家庭成员出生年月3','家庭成员联系电话3','家庭成员单位3',)
        ]
    
        for o in queryset:
            datadict.append(
            (o.id, o.xingming, o.xingbie, o.chushengnianyue, o.cangongshijian, o.baoxianhao, o.renshikahao, o.shenfenzhenghao, o.zhuzhi, o.jiguan,
             o.wenhuachengdu, o.dyxl_yuanxiao, o.dyxl_zhuanye, o.dyxl_shangxueshijian,
             o.hxxl_yuanxiao, o.hxxl_zhuanye, o.hxxl_shangxueshijian,
             o.zhengzhimianmao, o.rudangtuanshijian, o.gongbie, o.gongzhong, o.zhiwu, o.danwei, o.lianxidianhua,
             o.jtcy_guanxi1, o.jtcy_xingming1, o.jtcy_chushengnianyue1, o.jtcy_lianxidianhua1, o.jtcy_danwei1,
             o.jtcy_guanxi2, o.jtcy_xingming2, o.jtcy_chushengnianyue2, o.jtcy_lianxidianhua2, o.jtcy_danwei2,
             o.jtcy_guanxi3, o.jtcy_xingming3, o.jtcy_chushengnianyue3, o.jtcy_lianxidianhua3, o.jtcy_danwei3,
             )
        )

        c = Context({
            'data': datadict,
        })
        result = t.render(c)
        result = result .encode('utf8')
        response.write(result)
        return response
    

admin.site.register(Gongzhong, GongzhongAdmin)
admin.site.register(Zhiwu, ZhiwuAdmin)
admin.site.register(Yuangong, YuangongAdmin)
