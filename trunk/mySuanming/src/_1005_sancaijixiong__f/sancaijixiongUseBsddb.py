#coding=utf-8
"""
    高飞    于2009年5月16日
    更新到svn目录之后请更改数据库名称，否则将无法使用
"""
import csv,bsddb
hanzibihuaBsddbName='/home/crackpot/workspace/mySuanming/src/hanzibihuaBsddb.db'
suanmingBsddbName='/home/crackpot/workspace/mySuanming/src/suanmingBsddb.db'

def checkDb():
#    hanzibihuaBsddb=bsddb.btopen(hanzibihuaBsddbName,'r')
#    for k,v in hanzibihuaBsddb.iteritems():
#        print k,v
#    pass
#    hanzibihuaBsddb.close()

    suanmingBsddb=bsddb.btopen(suanmingBsddbName,'r')
    for k,v in suanmingBsddb.iteritems():
        if k[:k.find('_')]=='1005':
            print '%s==>%s'%(k,v)     
    suanmingBsddb.close()

def getWuxing():
    name='诸葛亮'
    global wuxing
    sumBihua=0
    hanzibihuaBsddb=bsddb.btopen(hanzibihuaBsddbName,'r')
    #print name,len(name)
    uniName=unicode(name)
    #print uniName,len(uniName)
    zishu=len(uniName)      #姓名中有几个字数
    listBihua=[]
    for i in range(len(uniName)):
        bihuashu=hanzibihuaBsddb[uniName[i].encode('utf-8')]
        listBihua.append(bihuashu)       #将汉字在数据库中查询并返回它的笔画数
        #print '%s,%d'%(uniName[i],int(listBihua[i]))#,uniName[i].encode('utf-8'))
    for i in range(len(listBihua)):
        #print listBihua[i]
        sumBihua+=int(listBihua[i])
    #print '您输入的姓名为：%s,字数为：%d，笔画总数为：%d'%(uniName,len(uniName),sumBihua)
    print '您输入的姓名为：%s'%(uniName)

    if zishu==2:
        #print '姓名中有2汉字'
        shu1=int(listBihua[0])+1
        shu1=isLiangweishu(shu1)
        #print shu1
        #print typeWuxing(shu1)
        shu2=int(listBihua[0])+int(listBihua[1])
        shu2=isLiangweishu(shu2)
        #print shu2
        #print typeWuxing(shu2)        
        shu3=int(listBihua[1])+1
        shu3=isLiangweishu(shu3)
        #print shu3
        #print typeWuxing(shu3)
        wuxing=typeWuxing(shu1)+typeWuxing(shu2)+typeWuxing(shu3)
        #print wuxing 
        return wuxing 
        #pass
    elif zishu==3:
        #print '姓名中有3个汉字'
        shu1=int(listBihua[0])
        shu1=isLiangweishu(shu1)
        #print shu1
        #print typeWuxing(shu1)
        shu2=int(listBihua[0])+int(listBihua[1])
        shu2=isLiangweishu(shu2)
        #print shu2
        #print typeWuxing(shu2)        
        shu3=int(listBihua[1])+int(listBihua[2])
        shu3=isLiangweishu(shu3)
        #print shu3
        #print typeWuxing(shu3)
        wuxing=typeWuxing(shu1)+typeWuxing(shu2)+typeWuxing(shu3)
        #print wuxing 
        return wuxing 
        #pass
    elif zishu==4:
        print '姓名中有4个汉字'
        shu1=int(listBihua[0])+int(listBihua[1])
        shu1=isLiangweishu(shu1)
        #print shu1
        #print typeWuxing(shu1)
        shu2=int(listBihua[1])+int(listBihua[2])
        shu2=isLiangweishu(shu2)
        #print shu2
        #print typeWuxing(shu2)        
        shu3=int(listBihua[2])+int(listBihua[3])
        shu3=isLiangweishu(shu3)
        #print shu3
        #print typeWuxing(shu3)
        wuxing=typeWuxing(shu1)+typeWuxing(shu2)+typeWuxing(shu3)
        #print wuxing 
        return wuxing 
        #pass
    else:
        pass 

    print isLiangweishu(10)
    
    
def isLiangweishu(shu):
    if shu>9:
        shu=shu%10
    else:
        pass
    return shu 

def typeWuxing(shu):
    #1 2 = 木   3 4 = 火 5 6 = 土 7 8 = 金 9 0 = 水
    if shu==1 or shu==2:
        wuxing='木'
    elif shu==3 or shu==4:
        wuxing='火'
    elif shu==5 or shu==6:
        wuxing='土'
    elif shu==7 or shu==8:
        wuxing='金'
    elif shu==9 or shu==0:
        wuxing='水'
    else:
        pass
    return wuxing

def getResult(wuxing):
    print '您的姓名对应五行为：',wuxing
    suanmingBsddb=bsddb.btopen(suanmingBsddbName,'r')
    key='1005_'+wuxing
    try:
        print '解析：',suanmingBsddb[key]
    except Exception,e:
        #print e,key
        print '对不起，系统中没有与您姓名相对应的五行类型'
    suanmingBsddb.close()

#checkDb()
getWuxing()
getResult(wuxing)