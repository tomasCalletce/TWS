def headHandle(arr):
    if arr[1] == '/image_user_one':
        header = 'HTTP/1.0 200 Page/File Not Found\n\n'
        return header.encode('utf-8')
    else:
        header = 'HTTP/1.0 400 Bad Request\n\n'
        return header.encode('utf-8')