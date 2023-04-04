from requestHandelers.GEThandler import handle

def handleClient(clientConnection, clientAddress):
    print('NEW CONNECTION => from %s:%s' % (clientConnection, clientAddress))

    request = clientConnection.recv(1024).decode()
    print('REQUEST => %s' % request)

    # esto hay que cambiarlo porque simpre responde con get y con codigo OK
    response = 'HTTP/1.0 200 OK\n\n' 

    if request.startswith("GET"):
        response += handle()

    # para hacer test usa postman con el link http://localhost:8000. no importa el request type.
    clientConnection.sendall(response.encode())
    clientConnection.close()

