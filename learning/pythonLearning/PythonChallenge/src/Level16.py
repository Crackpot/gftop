#coding=utf-8
'''
http://www.pythonchallenge.com/pc/return/mozart.html
'''
import Image
# # Download the image from: http://www.pythonchallenge.com/pc/return/mozart.gif  
def straighten(source):
    target=source.copy()
    for y in range(source.size[1]):
        line=[source.getpixel((x,y))for x in range(source.size[0])]
        pink=line.index(195)
        line=line[pink:]+line[:pink]
        for x,pixel in enumerate(line):
            target.putpixel((x,y),pixel)
    return target
out=straighten(Image.open('Level16.gif'))
out.save('Level16_result.gif')