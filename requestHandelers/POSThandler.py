
from utils.postUtils import extract_body

def postHandle(arr):
    try:
        result = {}

        reqbody = extract_body(arr)
        if arr[1] == "/createUser":
            if "Nombre" not in reqbody:
                header ='HTTP/1.0 400 Bad Request\n\n'
                result['header'] = header
                result['response'] = header.encode('utf-8')
            else:
                print("USER_CREATED: " + reqbody["Nombre"])
                header = "HTTP/1.1 201 Created\r\nContent-Type: text/plain; charset=UTF-8\r\nContent-Length: 0\r\nConnection: close\r\n\r\n"
                result['header'] = header
                result['response'] = header.encode('utf-8')
        else:
            header = 'HTTP/1.0 404 Page/File Not Found\n\n'
            result['header'] = header
            result['response'] = header.encode('utf-8')
        return result
    except Exception as e:
        header ='HTTP/1.0 400 Bad Request\n\n'
        result['header'] = header
        result['response'] = header.encode('utf-8')
        return result
