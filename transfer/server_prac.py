import socket
import os
import time


# 서버 소켓 오픈

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("", 5000))
server_socket.listen(5)

print("TCPServer Waiting for client on port 5000")

while True:
    # 클라이언트 요청 대기중 .
    client_socket, address = server_socket.accept()
    # 연결 요청 성공
    print("I got a connection from ", address)

    filename_list = [101, 102, 103, 104, 105, 106, 107, 108, 109, 110]  
    # 이미지파일이름을 변경하면 리스트안에 멤버들의 값도 이미지 파일의 이름과 같게 설정하면됨
    file_count = len(filename_list)
    client_socket.send(b'%d' % file_count)

    rec = client_socket.recv(1024)
    print(rec)

    print('전송완료')
    