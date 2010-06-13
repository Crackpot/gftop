#coding=utf-8
'''
http://www.pythonchallenge.com/pc/hex/bin.html

From: leopold.moz@pythonchallenge.com
Subject: what do you mean by "open the attachment?"
Mime-version: 1.0
Content-type: Multipart/mixed; boundary="===============1295515792=="

It is so much easier for you, youngsters.
Maybe my computer is out of order.
I have a real work to do and I must know what's inside!

--===============1295515792==
Content-type: audio/x-wav; name="indian.wav"
Content-transfer-encoding: base64
数据在Level19.txt中
'''
def handler1():
    import base64,wave,array
    # Input ...  
       
    dataFile = open("Level19.txt")  
    a = array.array("c", base64.b64decode(dataFile.read()))  
    a.byteswap()  
    dataFile.close()  
       
    # ... Processing ...  
       
    h = wave.open("Level19.wav", "wb")  
    h.setnchannels(1)  
    h.setsampwidth(1)  
    h.setframerate(22050)  
       
    # ... Output  
       
    h.writeframes(a.tostring())  
    h.close()  

handler1()