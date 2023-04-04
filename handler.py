import socket

def handleClient(clientConnection, clientAddress):
    print('NEW CONNECTION => from %s:%s' % (clientConnection, clientAddress))

    request = clientConnection.recv(1024).decode()
    print('REQUEST => %s' % request)

    # aqui va la logica real 
    # tambien falta ver como usar la lib threading porque este solo puede con un request a la vez.
    # para hacer test usa postman con el link http://localhost:8000. no importa el request type.
    response = 'HTTP/1.0 200 OK\n\nque mas'
    clientConnection.sendall(response.encode())
    clientConnection.close()