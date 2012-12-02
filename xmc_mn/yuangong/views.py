#coding=utf8
from django.core.context_processors import csrf
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import loader
from django.template.context import Context
from yuangong.models import Yuangong

def index(request):
    yuangong_list = Yuangong.objects.all()
    paginator = Paginator(yuangong_list, 1) # Show 25 yuangongs per page

    page = request.GET.get('page')
    try:
        yuangongs = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        yuangongs = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        yuangongs = paginator.page(paginator.num_pages)

    #内容
    c = {"yuangongs":yuangongs}
    c.update(csrf(request))
    return render_to_response('yuangong/index.html',c)

def output(request):
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=%s' % 'yuangong.csv'
    t = loader.get_template('yuangong/csv.html')
    objs = Yuangong.objects.all()
    datadict = [
        ('id','姓名','性别','出生年月','参加工作时间', '劳动保险号','人事卡号', '身份证号', '详细住址', '籍贯',
         '文化程度','第一学历毕业院校','专业','上学时间',
         '后续学历毕业院校','后续学历专业','后续学历上学时间',
         '政治面貌', '入党团时间', '工别', '工种', '职务', '单位', '联系电话',
         '家庭成员关系1','家庭成员姓名1','家庭成员出生年月1','家庭成员联系电话1','家庭成员单位1',
         '家庭成员关系2','家庭成员姓名2','家庭成员出生年月2','家庭成员联系电话2','家庭成员单位2',
         '家庭成员关系3','家庭成员姓名3','家庭成员出生年月3','家庭成员联系电话3','家庭成员单位3',
         )
    ]
    
    for o in objs:
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

def upload(request):
    file_obj = request.FILES.get('file', None)
    if file_obj:
        import csv
        import StringIO
        buf = StringIO.StringIO(file_obj['content'])
        try:
            reader = csv.reader(buf)
        except:
            return render_to_response('address/uploaderror.html',
                {'message':'你需要上传一个csv格式的文件！'})
        for row in reader:
#            objs = Address.objects.get_list(name__exact=row[0])
            objs = Yuangong.objects.filter(xingming=row[0])
            if not objs:
                obj = Yuangong(
                    xingming=row[0], xingbie=row[1], chushengnianyue=row[2], cangongshijian=row[0], baoxianhao=row[0], renshikahao=row[0], shenfenzhenghao=row[0], zhuzhi=row[0], jiguan=row[0],
             wenhuachengdu=row[0], dyxl_yuanxiao=row[0], dyxl_zhuanye=row[0], dyxl_shangxueshijian=row[0],
             hxxl_yuanxiao=row[0], hxxl_zhuanye=row[0], hxxl_shangxueshijian=row[0],
             zhengzhimianmao=row[0], rudangtuanshijian=row[0], gongbie=row[0], gongzhong=row[0], zhiwu=row[0], danwei=row[0], lianxidianhua=row[0],
             jtcy_guanxi1=row[0], jtcy_xingming1=row[0], jtcy_chushengnianyue1=row[0], jtcy_lianxidianhua1=row[0], jtcy_danwei1=row[0],
             jtcy_guanxi2=row[0], jtcy_xingming2=row[0], jtcy_chushengnianyue2=row[0], jtcy_lianxidianhua2=row[0], jtcy_danwei2=row[0],
             jtcy_guanxi3=row[0], jtcy_xingming3=row[0], jtcy_chushengnianyue3=row[0], jtcy_lianxidianhua3=row[0], jtcy_danwei3=row[0],
 
                    )
            else:
                obj = objs[0]
                obj.gender = row[1]
                obj.telphone = row[2]
                obj.mobile = row[3]
                obj.room = row[4]
            obj.save()

        return HttpResponseRedirect('/yuangong/')
    else:
        return render_to_response('yuangong/uploaderror.html',
            {'message':'你需要上传一个文件！'})