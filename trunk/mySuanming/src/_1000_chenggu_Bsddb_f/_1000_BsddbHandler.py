#coding=utf-8
import bsddb, os, csv
#dbName='/home/crackpot/workspace/mySuanming/src/suanmingBsddb.db'
suanmingBsddbName = '/home/workspace/gftop/mySuanming/src/bsddb/suanmingBsddb.db'

def checkDb():
    suanmingBsddb = bsddb.btopen(suanmingBsddbName, 'r')
    for k, v in suanmingBsddb.iteritems():
        if k[:k.find('_')] == '1000':
            print '%s==>%s' % (k, v)     
    suanmingBsddb.close()
    
def getSourceAndModifyBsddb():
    suanmingBsddb = bsddb.btopen(suanmingBsddbName, 'r')
    suanmingBsddb = bsddb.btopen(suanmingBsddbName, 'w')
    myfile = open('chenggu.db', 'r')       #总分    结果
    reader = csv.reader(myfile)
    dictScore = {}
    for row in reader:      #文件中的每一行
        #print row 
        listCase = []
        count = 0
        for item in row:        #每一行的各个元素
            #print count, item
            listCase.append(item)
            count += 1
        dictScore[listCase[0]] = listCase[1]
    for k, v in dictScore.items():       #总分        详解
        #print k,v
        key = '1000_' + k
        suanmingBsddb[key] = v
        pass
    myfile.close()
    #－－－－－－－－
    myfile1 = open('chenggu1.db', 'r')     #年份    分数1
    reader1 = csv.reader(myfile1)
    dictY = {}
    for row in reader1:      #文件中的每一行
        #print row 
        listCase = []
        count = 0
        for item in row:        #每一行的各个元素
            #print count, item
            listCase.append(item)
            count += 1
        dictY[listCase[0]] = listCase[1]
    for k, v in dictY.items():
        key = '1000_Y' + k
        print key, v
        #suanmingBsddb[key]=v
        pass
    myfile1.close()
    #－－－－－－－－
    myfile2 = open('chenggu2.db', 'r')     #月份    分数2
    reader2 = csv.reader(myfile2)
    dictM = {}
    for row in reader2:      #文件中的每一行
        #print row 
        listCase = []
        count = 0
        for item in row:        #每一行的各个元素
            #print count, item
            listCase.append(item)
            count += 1
        dictM[listCase[0]] = listCase[1]
    for k, v in dictM.items():
        key = '1000_M' + k
        print key, v
        #suanmingBsddb[key]=v
        pass
    myfile2.close()
    #－－－－－－－－
    myfile3 = open('chenggu3.db', 'r')     #日    分数3
    reader3 = csv.reader(myfile3)
    dictD = {}
    for row in reader3:      #文件中的每一行
        #print row 
        listCase = []
        count = 0
        for item in row:        #每一行的各个元素
            #print count, item
            listCase.append(item)
            count += 1
        dictD[listCase[0]] = listCase[1]
    for k, v in dictD.items():
        key = '1000_D' + k
        print key, v
        suanmingBsddb[key] = v
        pass
    myfile3.close()
    #－－－－－－－－
    myfile4 = open('chenggu4.db', 'r')     #时    分数4
    reader4 = csv.reader(myfile4)
    dictH = {}
    for row in reader4:      #文件中的每一行
        #print row 
        listCase = []
        count = 0
        for item in row:        #每一行的各个元素
            #print count, item
            listCase.append(item)
            count += 1
        dictH[listCase[0]] = listCase[1]
    for k, v in dictH.items():
        key = '1000_H' + k
        print key, v
        suanmingBsddb[key] = v
        pass
    suanmingBsddb.sync()
    suanmingBsddb.close()


checkDb()
#getSourceAndModifyBsddb()
