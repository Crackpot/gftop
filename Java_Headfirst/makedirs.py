#coding=utf-8
import os
startChapter = 1
endChapter = 19
for i in range(startChapter,endChapter):
    if i < 10:
        str_i = "0" + str(i)
    else:
        str_i = str(i)
    path = './ch'+str_i
    if not os.path.exists(path):
        print "创建路径 ./ch"+str_i
        os.mkdir(path)
