from requestHandelers.GEThandler import handle
import json
def extract_body(arr):
    # Join the array into a single string
    request_string = ' '.join(arr)

    # Find the starting and ending indices of the JSON object
    start_index = request_string.find('{')
    end_index = request_string.rfind('}') + 1

    # Extract the JSON object string and parse it
    json_object_str = request_string[start_index:end_index]
    json_object = json.loads(json_object_str)

    return json_object
def handleClient(clientConnection, clientAddress):
    # print('NEW CONNECTION => from %s:%s' % (clientConnection, clientAddress))

    request = clientConnection.recv(1024).decode()
    # print('REQUEST => %s' % request)

    # esto hay que cambiarlo porque simpre responde con get y con codigo OK
    response = 'HTTP/1.0 200 OK\n\n' 
    arr = request.split(' ')
    # print( arr)

    # print(request)
    # print (request.startswith('GET'))
    if request.startswith("GET"):
        if arr[1] == "/getFile":#Caso 1
            print("getting file...")
            response += handle()
        elif arr[1] == '/getHtml':#Caso 2
            print("getting Html...")
            response += handle()
        else:
            response = 'HTTP/1.0 404 Page/File Not Found\n\n'
    elif request.startswith("POST"):
        try:
            reqbody = extract_body(arr)
            if arr[1] == "/createUser":#Caso 1
                print("Creating User...")
                if "Nombre" not in reqbody:
                    response = 'HTTP/1.0 400 Bad Request\n\n'
                else:
                    print(reqbody["Nombre"])
            else:
                response = 'HTTP/1.0 404 Page/File Not Found\n\n'
        except e :
            reponse='HTTP/1.0 400 Bad Request\n\n'
        

    elif request.startswith("HEAD"):
        if arr[1] != "/tomas" and arr[1] != '/juan' :#Caso 1
            response = 'HTTP/1.0 404 Page/File Not Found\n\n'
    else:
        response = 'HTTP/1.0 400 Bad Request\n\n'

    # elif request.startswith("POST"):

    # para hacer test usa postman con el link http://localhost:8000. no importa el request type.
    clientConnection.sendall(response.encode())
    clientConnection.close()

