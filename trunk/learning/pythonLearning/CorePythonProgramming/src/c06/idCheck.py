#coding=utf-8
import string
alphas=string.letters+'_'
nums=string.digits
string=raw_input('请输入标识符')
if len(string)>1:
    if string[0] not in alphas:
        print '无效标识符'
    else:
        print '有效标识符'