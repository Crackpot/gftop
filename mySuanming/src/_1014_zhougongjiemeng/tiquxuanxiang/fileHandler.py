#coding=utf-8
myfile=open('source','r')
tmp=open('tmp','w')
for eachline in myfile.readlines():
    print eachline
    #<option value="volvo">Volvo</option>
    eachline='        <option>'+eachline+'</option>\n'
    tmp.write(eachline)
    
    
myfile.close