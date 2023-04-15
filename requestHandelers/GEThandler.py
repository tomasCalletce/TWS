from utils.main import getFile

def getHandle(arr):
    if arr[1] == "/page_one":
        page  = getFile('pageOne.html',"r")

        headers= f"HTTP/1.1 200 OK\r\nContent-Length: {len(page)}\r\nContent-Type: text/html; charset=UTF-8\r\nConnection: close\r\n\r\n"

        response = headers + page
        return  response.encode('utf-8')

    elif arr[1] == '/page_two':
        page  = getFile('pageTwo.html',"r")

        headers= f"HTTP/1.1 200 OK\r\nContent-Length: {len(page)}\r\nContent-Type: text/html; charset=UTF-8\r\nConnection: close\r\n\r\n"

        response = headers + page
        return  response.encode('utf-8')
    elif arr[1] == '/page_three':
        page  = getFile('pageThree.html',"r")

        headers= f"HTTP/1.1 200 OK\r\nContent-Length: {len(page)}\r\nContent-Type: text/html; charset=UTF-8\r\nConnection: close\r\n\r\n"

        response = headers + page
        return  response.encode('utf-8')
    elif arr[1] == '/page_four':
        page  = getFile('pageFour.html',"r")

        headers= f"HTTP/1.1 200 OK\r\nContent-Length: {len(page)}\r\nContent-Type: text/html; charset=UTF-8\r\nConnection: close\r\n\r\n"

        response = headers + page
        return  response.encode('utf-8')

    elif arr[1] == '/image_user_one':
        image  = getFile('user1.jpg',"rb")

        headers= f"HTTP/1.1 200 OK\r\nContent-Length: {len(image)}\r\nContent-Type: image/jpeg\r\nConnection: close\r\n\r\n"

        return  headers.encode('utf-8') + image
    elif arr[1] == '/image_user_two':
        image  = getFile('user2.jpg',"rb")

        headers= f"HTTP/1.1 200 OK\r\nContent-Length: {len(image)}\r\nContent-Type: image/jpeg\r\nConnection: close\r\n\r\n"

        return  headers.encode('utf-8') + image
    elif arr[1] == '/big_file':
        textFile  = getFile('bigFile.txt',"rb")

        headers= f"HTTP/1.1 200 OK\r\nContent-Length: {len(textFile)}\r\nContent-Type: text/plain; charset=UTF-8\r\nContent-Disposition: attachment; filename=large_file.txt\r\nConnection: close\r\n\r\n"

        return  headers.encode('utf-8') + textFile
    else:
        headers= 'HTTP/1.0 404 Page/File Not Found\n\n'
        return headers.encode('utf-8')
