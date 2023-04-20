import socket
import threading

import handler

SERVER_HOST = '0.0.0.0'
print('Give Port Name: ')

SERVER_PORT = int(input())

#AF_INET == IPv6 Socket type Sock_Stream (Streams using TCP transportation protocol)
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serverSocket.bind((SERVER_HOST, SERVER_PORT))#Socket parameters (HOSTIP,PORT)
serverSocket.listen(1)
#defines how many unaccepted devices the server allows
#it specifies the number of unaccepted connections that the system will allow before refusing new connections
print('ACTIVE PORT => %s' % SERVER_PORT)

while True:    
    clientConnection, clientAddress = serverSocket.accept()
    #Threading 
    thread = threading.Thread(target= handler.handleClient, args=(clientConnection, clientAddress))
    thread.start()


