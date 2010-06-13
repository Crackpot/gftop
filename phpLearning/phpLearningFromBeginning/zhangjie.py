myfile=open('U5.txt')
for row in myfile.readlines():
    #print row
    line="<tr><td><a href=./\""+row+">"+row+"\"</a></td></tr>"
    print line
