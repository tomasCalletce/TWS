from utils.main import getFile

def headHandle(arr):
    if arr[1] == '/image_user_one':
        file = getFile('user1.jpg',"rb")
        header = f"HTTP/1.1 200 OK\r\nContent-Type: image/jpeg\r\nContent-Length: {len(file)}\r\nConnection: close\r\n\r\n"
        return header.encode('utf-8')
    elif arr[1] == '/image_user_two':
        file = getFile('user2.jpg',"rb")
        header = f"HTTP/1.1 200 OK\r\nContent-Type: image/jpeg\r\nContent-Length: {len(file)}\r\nConnection: close\r\n\r\n"
        return header.encode('utf-8')
    else:
        header = "HTTP/1.1 400 Bad Request\r\nContent-Type: text/plain; charset=UTF-8\r\nContent-Length: 0\r\nConnection: close\r\n\r\n"
        return header.encode('utf-8')