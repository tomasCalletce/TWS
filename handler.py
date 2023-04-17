from utils.loggerUtils import getLogger, writeLogger
from requestHandelers.GEThandler import getHandle
from requestHandelers.POSThandler import postHandle
from requestHandelers.HEADhandler import headHandle
import io
import json
def handleClient(clientConnection, clientAddress):
    # print('NEW CONNECTION => from %s:%s' % (clientConnection, clientAddress))

    request = clientConnection.recv(1024).decode()
    # print('REQUEST => %s' % request)


    response = b''
    arr = request.split(' ')

    if request.startswith("GET"):
        response = getHandle(arr)
    elif request.startswith("POST"):
        response = postHandle(arr)
    elif request.startswith("HEAD"):
        response = headHandle(arr)

    data = getLogger()
    data["list"].append(request)
    data["list"].append(response['header'])
    writeLogger(data)

    clientConnection.sendall(response['response'])
    clientConnection.close()

