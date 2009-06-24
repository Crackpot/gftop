# -*- coding: utf-8 -*- 
'''常用方法'''
import types

def args2str(args={}):
    '''
    {'age': ['11', ], 'name': ['echo', ]}
    '''
    ret = ''
    if args and type(args) == types.DictType:
        tmp = []
        for k,v in args.items():
            if type(v) in (types.ListType, types.TupleType):
                for _vitem in v:
                    _itmp = '%s=%s' % (str(k), str(_vitem))
                    tmp.append(_itmp)
            else:
                _itmp = '%s=%s' % (str(k), str(v))
                tmp.append(_itmp)
                
        ret = '&'.join(tmp)
    
    return ret


import re
phonere = re.compile(r'^1[3|5|8]\d{9}$')
numre = re.compile(r'^\d+$')
def create_sm_verifycode(phone, stn):
    '''生成算命验证吗
    phone: 手机号码
    stn: 算命子产品编号
    '''
    if not phonere.match(phone):
        msg = '-1'
        return msg

    if not numre.match(stn):
        return '-1'


    stn = int(stn)

    verifycode = ''
    _verifycode_list = []
    for i in xrange(1, 8, 2):
        _verifycode_list.append(phone[i])


    verifycode = int(''.join(_verifycode_list))
   
    _tmp = verifycode + stn

    ret = str(_tmp)[-4:]
    return ret
