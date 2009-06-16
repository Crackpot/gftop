import socket
clientsocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientsocket.connect(('localhost',8001))
while 1:
    data=raw_input('>')
    clientsocket.send(data)
    if not data:
        break
    newdata=clientsocket.recv(1024)
    print newdata
clientsocket.close()