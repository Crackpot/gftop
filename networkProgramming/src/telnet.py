import socket
serversocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serversocket.bind(('localhost',8000))
serversocket.listen(1)
clientsocket,clientaddress=serversocket.accept()
print 'Connection from ',clientaddress
while 1:
    data=clientsocket.recv(1024)
    if not data:
        break
    clientsocket.send(data)
clientsocket.close()
