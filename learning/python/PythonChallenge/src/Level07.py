#coding=utf-8
import Image,re
image=Image.open('Level07.png')
print "Image info:",image.format, image.size, image.mode
y=0
while y<image.size[1]:
    pixel=image.getpixel((0,y))
    if pixel[0]==pixel[1]==pixel[2]:
        break
    y+=1
    print y
ans=[]
x=0
while x<image.size[0]:
    pixel=image.getpixel((x,y))
    if not pixel[0]==pixel[1]==pixel[2]:
        break
    ans.append(chr(pixel[0]))
    x+=7
print ''.join(ans)
print ''.join([chr(int(v))for v in re.findall('[0-9]+',''.join(ans))])