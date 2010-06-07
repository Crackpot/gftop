#coding=utf-8
import csv,codecs,random
"""
    高飞    于2009年5月11日
"""
def getDicts():
    myfile=open('mobile_num_jixiong.db','r')
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
#    #print dictExplanation
#    print '----存放详解的字典----'
#    for k,v in dictExplanation.items():
#        print k,v
#    print '\n\n----存放分析的字典----'
#    for k,v in dictAnalysis.items():
#        print k,v
    myfile.close()

def getRemainder():
    #telNum=int(raw_input('请输入您的手机号码：'))
    telNum=15803516966
    #telNum=random.randrange(10000000000,20000000000)
    remainder=telNum%80
    print '您输入的手机号码是',telNum#,'余数是：',remainder
    shiweishu=remainder/10
    geweishu=remainder%10
    #print '余数的个位数为%d,十位数为%d'%(shiweishu,geweishu)
    global factOfExplanation        #详解因数
    factOfExplanation=shiweishu+geweishu
    if factOfExplanation>9:     #详解的键值为0到9，大于9则无效
        factOfExplanation=factOfExplanation-10
    #print '详解因数为：%d'%factOfExplanation
    global factOfAnalysis       #分析因数
    factOfAnalysis=remainder
    #print '分析因数为：%d'%factOfAnalysis
    return factOfAnalysis,factOfExplanation
def getResults(factOfExplanation,factOfAnalysis):
    print '详解：%s'%dictExplanation[str(factOfExplanation)]
    print '分析：%s'%dictAnalysis[str(factOfAnalysis)]



getDicts()
getRemainder()
getResults(factOfExplanation, factOfAnalysis)
