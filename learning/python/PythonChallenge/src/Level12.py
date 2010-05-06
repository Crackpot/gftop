#coding=utf-8
'''
http://www.pythonchallenge.com/pc/return/evil.html
'''
import Image
from cStringIO import StringIO

s = open("Level12.gfx", "rb").read()
for i in range(5):
    piece = s[i::5]  # every fifth byte, starting at i
    im = Image.open(StringIO(piece))
    f = open("Level12_%d.%s" % (i, im.format.lower()), "wb")
    f.write(piece)
    f.close()
'''
dis
pro
port
ional
ity
disproportional
'''