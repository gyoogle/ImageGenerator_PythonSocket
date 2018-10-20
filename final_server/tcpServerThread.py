import socket, threading
from PIL import Image, ImageFile
import os
import io
import struct

ImageFile.LOAD_TRUNCATED_IMAGES = True

class TCPServerThread(threading.Thread):
    def __init__(self, tcpServerThreads, connections, connection, clientAddress):
        threading.Thread.__init__(self)
 
        self.tcpServerThreads = tcpServerThreads
        self.connections = connections
        self.connection = connection
        self.clientAddress = clientAddress
 
    def run(self):
        try:
            
            #바이트로 바꾼 이미지 받는 부분
            #byte_image = self.connection.recv(65536)
            #print('tcp server(client) :: bytes image : ', byte_image)
            
            #height, width 배열 값 저장위한 변수 선언
            height = self.connection.recv(1024)
            print('height : ', height.decode())
            width = self.connection.recv(1024)
            print('width : ', width.decode())

            int_height = int(height.decode())
            int_width = int(width.decode())

            print('(', int_height, ',', int_width, ')')
            print("height, width 전송 완료")
            '''
            while True:
                img_data = self.connection.recv(65536)
                data = img_data
                if img_data:
                    while img_data:
                        print("recving data..")
                        img_data = self.connection.recv(65536)
                        data += img_data
                    else:
                        break

           
            try:
                byte_size = self.connection.recv(10240)
            except Exception as e:
                print(e)
            int_size = int(byte_size.decode())
            print('tcp server(client) :: bytes size 길이 : ', byte_size.decode())
            
            byte_image = self.connection.recv(92492)
            print('tcp server(client) :: bytes image 길이 : ', len(byte_image))
            
            #이미지 바이트 클라이언트에게 보내기
            self.connection.sendall(byte_image)
            print('전송한 이미지 바이트 :', len(byte_image))
            self.connection.sendall(width)
            self.connection.sendall(height)
             '''

            buf = b''
            while len(buf)<4:
                buf += self.connection.recv(4-len(buf))
            size = struct.unpack('!i', buf)
            print("receiving %s bytes" % size)
            '''
            with open('tst2.jpg', 'wb') as img:
                while True:
                    data = self.connection.recv(1024)
                    if not data:
                        break
                    img.write(data)
            print('received, yay!')
            '''
            byte_image = b''
            while True:
                data = self.connection.recv(1024)
                if not data:
                    break
                byte_image += data
            print('received, yay!')
            print(len(byte_image))

            
            #print("전송 완료. 바이트 이미지 복원하시겠습니까?(y/n)")
            ans = input('전송 완료. 바이트 이미지 복원하시겠습니까?(y/n) : ')

            if(ans == 'y'):
                try:
                    #print(byte_image)
                    print("이미지 복원 중")
                    image = Image.open(io.BytesIO(byte_image))
                    #image.save('save_image.bmp')
                    image = image.resize((int_width, int_height), Image.ANTIALIAS)
                    print("복원 완료!")
                    #bytearray(image2.read())
                    image.show()
                    print("클라이언트에 전송 완료")
                except Exception as e:
                    print(e)
                    
            print('tcp server(client) :: exit!!')
            print('tcp server :: server wait...')
            
        except:
            self.connections.remove(self.connection)
            self.tcpServerThreads.remove(self)
            exit(0)
        self.connections.remove(self.connection)
        self.tcpServerThreads.remove(self)
 
    def send(self, message):
        print('tcp server :: ',message)
        try:
            for i in range(len(self.connections)):
                self.connections[i].sendall(message.encode())
        except:
             pass