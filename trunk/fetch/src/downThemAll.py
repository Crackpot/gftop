#coding=utf-8
#自动下载功能
import os, time, random

def mkdirs(path):
    '''
    建立多级目录
    例如
    mkdirs('/tmp/s/s/ss/dd')
    '''
    if os.path.exists(path):
        return 
 
    paths=path.split('/')
    p='';
    for i in range(0,len(paths)):
        p=p+ paths[i]+'/'
        print p
        if not os.path.exists(p):
            os.mkdir(p)

def downThemAll():
    path=raw_input('请输入要保存文件的位置，请确保它存在(例：/home/crackpot/Desktop/rings/)\n')
    if os.path.exists(path):
#        checkPower(path)
        #当前日期
        today=time.strftime('%Y%m%d')
        path=path+today+'/'
        checkPower(path)

        #mkdirs(path)
        songDict={'beyond- \xe5\xad\xa4\xe5\x8d\x95\xe4\xb8\x80\xe5\x90\xbb': 'http://content.12530.com/cmsdata/batchmusic/20070724/1USyjC2S.wma', 'beyond- \xe6\x97\xa0\xe4\xba\x8b\xe6\x97\xa0\xe4\xba\x8b': 'http://content.12530.com/newcmsdata/batchmusic/20080707/MdoKwSGd.wma', 'beyond- \xe5\x86\x8d\xe8\xa7\x81\xe7\x90\x86\xe6\x83\xb3': 'http://content.12530.com/cmsdata/batchmusic/20070724/jfaH3gKp.wma', 'beyond- \xe5\x8d\x88\xe5\xa4\x9c\xe8\xbf\xb7\xe5\xa2\x99': 'http://content.12530.com/cmsdata/batchmusic/20070724/lg3kJEja.wma', 'beyond- \xe6\x88\x91\xe7\x9a\x84\xe7\x9f\xa5\xe5\xb7\xb1': 'http://content.12530.com/newcmsdata/batchmusic/20080707/y9zHYEvF.wma'}
        count=1
        
        for k,v in songDict.items():
            url=v
            #文件扩展名
            ext = url[(len(url)-3):]

            #时间戳
            timeStamp=str(int(time.time()))
            #4位随机数
            randomSeed='%#04d' % random.randint(1,1000)
            #文件名
            fileName=path+timeStamp+randomSeed+'.'+ext
            songDict[k]=fileName
            #url='http://content.12530.com/cmsdata/batchmusic/20070724/eQHavC5W.wma'
            print '\n下载第%d首铃声：'%count
            cmd='axel -o '+fileName+' '+url
            os.system(cmd)
            count=count+1
            print '保存为%s'%fileName
        print '\n下载任务完成！'
        print '\n将歌曲信息写入csv文件中……\n'
        content=''
        for k,v in songDict.items():
            print k,v  
            singer=k[:k.find('-')]
            songName=k[(k.find('- ')+2):]
            songUrl=v
            content=content+singer+','+songName+','+songUrl+'\n'
        myfile=open('baiduRingsNow.csv','w')
        myfile.write(content)
        myfile.close()
    else:
        print '您输入的路径无效，请重新输入！'
        downThemAll()

#检测是否具有此路径的操作权限        
def checkPower(path):
    #留着接口，有机会完善
    #创建文件夹，看是否存在
    #print path
    pass
    

    

#检查是否要下载并
def flagDownThemAllCheck():
    flagDownThemAll=str(raw_input('是否下载全部文件？请输入y或n:'))
    if flagDownThemAll=='y':
        downThemAll()
    elif flagDownThemAll=='n':
        print '您选择不下载文件，本次操作结束！'
    else:
        print '您的输入有误，请重新输入：'
        flagDownThemAllCheck()
    
