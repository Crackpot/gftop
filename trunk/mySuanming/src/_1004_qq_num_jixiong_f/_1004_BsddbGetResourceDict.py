#coding=utf-8
import csv,codecs,random,bsddb
"""
    高飞    于2009年5月11日
"""

dbName='/home/crackpot/workspace/mySuanming/src/suanmingBsddb.db'

#suanmingBsddb=bsddb.btopen(dbName)
#suanmingBsddb=bsddb.btopen(dbName,'r')
suanmingBsddb=bsddb.btopen(dbName,'w')
def getDicts():
    myfile=open('qq_num_jixiong.db','r')
    reader=csv.reader(myfile)
    seqLine=0   #标记读的是第几行
    global  dictExplanation      #详解
    dictExplanation={}
    global  dictAnalysis
    dictAnalysis={}
    
    for row in reader:
        #print row        #无法显示中文
        #print type(row)    #row的类型是列表
        #print '行长度%d'%len(row)
        """
            分别对两个字典进行赋值
        """
        for item in row:        #详解的位置从5行到15行；分析的位置从16行到末尾（97行）
            seqLine=seqLine+1
            #print '%d\t%s'%(seqLine,item)
            posBranch=item.find('|')
            if seqLine in range(6,16):      #详解
                dictExplanation[item[:posBranch]]=item[posBranch:]
            elif seqLine>16:        #分析
                dictAnalysis[item[:posBranch]]=item[posBranch:]
    #解析字典
    #print dictExplanation
    #print '----存放详解的字典----'
    for k,v in dictExplanation.items():
        #print k,v
        print '1004_xj_'+k,v
        #suanmingBsddb['1004_xj_'+k]=v
    #print '\n\n----存放分析的字典----'
    for k,v in dictAnalysis.items():
        #print k,v
        print '1004_fx_'+k,v
        #suanmingBsddb['1004_fx_'+k]=v
    myfile.close()
        

    #suanmingBsddb['%s'%bsddbKey] = '%s'% listCase[1]

getDicts()


#遍历数据库文件
for k,v in suanmingBsddb.iteritems():
    if k[:k.find('_')]=='1004':
        print k,v
#suanmingBsddb.sync()
suanmingBsddb.close()