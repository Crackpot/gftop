#coding=utf-8
import gzip,difflib
'''
http://www.pythonchallenge.com/pc/return/balloons.html
'''
# Download the GNU zip file from:  
# http://www.pythonchallenge.com/pc/return/deltas.gz  
h=gzip.open('Level18.gz')
d=difflib.Differ()
part_1,part_2=[],[]
file_1,file_2,file_3=[],[],[]
for line in h:
    part_1.append(line[0:53])
    part_2.append(line[56:-1])
h.close()
for line in list(d.compare(part_1, part_2)):
    if line[0]=='+':
        file_1.append(line[2:])
    elif line[0]=='-':
        file_2.append(line[2:])
    else:
        file_3.append(line[2:])
for n,data in enumerate((file_1,file_2,file_3)):
    temp=[]
    for line in data:
        temp.extend([chr(int(o,16)) for o in line.strip().split(' ') if o])
    h=open("Level18_result_%s.png"%(n+1),'wb')
    h.writelines(temp)
    h.close()