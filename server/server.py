from PIL import Image
import io
import socket
import sys

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
    
    '''
    byte_image = conn.recv(65536)
    print('bytes image')
    print(byte_image)
    conn.sendall(byte_image)

    image = Image.open(io.BytesIO(byte_image)) # 바이트 이미지 다시 이미지로 만듬
    #image.show()
    '''
    while True:
      msg = conn.recv(1024)
      if not msg:
        break;
      print(msg.decode())

    '''
    stopper = 0
    while True:
      if (stopper == 0):
        print('height :', end=" ")
      elif (stopper == 1):
        print('width :', end=" ")
      elif (stopper > 1):
        break
      msg = conn.recv(1024)
      print(f'{msg.decode()}')
      conn.sendall(msg)
      stopper += 1
    '''
    conn.close()
    s.close()

if __name__ == '__main__':
  run_server()