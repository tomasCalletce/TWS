import socket
import handler

SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8000

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serverSocket.bind((SERVER_HOST, SERVER_PORT))
serverSocket.listen(1)
print('ACTIVE PORT => %s' % SERVER_PORT)

while True:    
    clientConnection, clientAddress = serverSocket.accept()
    handler.handleClient(clientConnection,clientAddress)

