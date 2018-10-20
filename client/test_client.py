#Client 예시
import socket
import sys
from PIL import Image
import os
import io
from array import array
import base64

host = '10.93.241.135'
port = 4000
addr = (host, port)

def run():
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
    try:
      s.connect(addr)
    except Exception as e:
      print('서버 (%s:%s)에 연결 할 수 없습니다.' % addr)
      sys.exit()
    print('서버 (%s:%s)에 연결 되었습니다.' % addr)

    fd = open('test1.png', "rb")
    b = bytearray(fd.read())
    c = str(len(b))
    
    print(c)
    print(c.encode())

    s.sendall(c.encode()) # 서버로 보내기
    s.sendall(b)

    s.close()

if __name__ == '__main__':
  run()