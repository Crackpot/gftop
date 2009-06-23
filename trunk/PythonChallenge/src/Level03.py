#coding=utf-8
'''
http://www.pythonchallenge.com/pc/def/equality.html
'''
import re
if __name__ == '__main__':    
    finpath = 'Level03.txt'
    with open(finpath) as fin:
        # translate text into a single string
        text = ''.join([line.rstrip() for line in fin.read()])
        pattern = re.compile(r'[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]')
        print(''.join(pattern.findall(text)))