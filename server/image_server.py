import socket
import sys
from PIL import Image
import os
import io
from array import array
import base64

pr = ['1.height', '2.width']

def run_server(port=4000):
  host = '172.20.10.6'

  #socket 생성
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print('socket created')
    
    #Bind
    try:
        s.bind((host, port))
    except socket.error as err:
        print ('Bind Failed', err)
        sys.exit()
    print ('Socket Bind Success!')
    
    #Listen
    s.listen(5)
    print ('Socket is now listening')

    conn, addr = s.accept()
    print("client = {}: {}".format(addr[0],addr[1]))
    
    fd = open('test1.png', "rb")
    b = bytearray(fd.read())
    conn.sendall(b) # 서버로 보내기
    print('바이트 이미지 전송 완료')
    fd.close()

    conn.close()
    s.close()

if __name__ == '__main__':
  run_server()