#coding=utf-8
'''
http://www.pythonchallenge.com/pc/return/bull.html
http://www.pythonchallenge.com/pc/return/sequence.txt
'''
a = [
    '1', 
    '11', 
    '21', 
    '1211', 
    '111221', 
]
def func(listOri):
    for item in listOri:        #列表中的每个数字
        for i in range(0,len(item)):        #数字中的每一位
            count=1
            tmp=item[i]
            print tmp,
        print 
func(a)