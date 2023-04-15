from requestHandelers.GEThandler import getHandle
from utils.postUtils import extract_body

def handleClient(clientConnection, clientAddress):
    # print('NEW CONNECTION => from %s:%s' % (clientConnection, clientAddress))

    request = clientConnection.recv(1024).decode()
    # print('REQUEST => %s' % request)

    response = b''
    arr = request.split(' ')

    if request.startswith("GET"):
        response = getHandle(arr)
    # elif request.startswith("POST"):
    #     try:
    #         reqbody = extract_body(arr)
    #         if arr[1] == "/createUser":#Caso 1
    #             print("Creating User...")
    #             if "Nombre" not in reqbody:
    #                 response = 'HTTP/1.0 400 Bad Request\n\n'
    #             else:
    #                 print(reqbody["Nombre"])
    #         else:
    #             response = 'HTTP/1.0 404 Page/File Not Found\n\n'
    #     except e :
    #         reponse='HTTP/1.0 400 Bad Request\n\n'
    # elif request.startswith("HEAD"):
    #     if arr[1] != "/tomas" and arr[1] != '/juan' :#Caso 1
    #         response = 'HTTP/1.0 404 Page/File Not Found\n\n'
    else:
        messege = 'HTTP/1.0 400 Bad Request\n\n'
        response = messege.encode('utf-8')

    # para hacer test usa postman con el link http://localhost:8000. no importa el request type.
    clientConnection.sendall(response)
    clientConnection.close()

