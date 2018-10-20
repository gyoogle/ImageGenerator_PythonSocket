# tcpServer Thread file (req/res data)

import socket, threading
from PIL import Image, ImageFile
import os
import io
import struct
import time

ImageFile.LOAD_TRUNCATED_IMAGES = True

class TCPServerThread(threading.Thread):
    
    # tcpServer.py에서 Client 정보 받기
    def __init__(self, tcpServerThreads, connections, connection, clientAddress):
        threading.Thread.__init__(self)
 
        self.tcpServerThreads = tcpServerThreads
        self.connections = connections
        self.connection = connection
        self.clientAddress = clientAddress

    # thread 실행
    def run(self):
        
        try:

            # Client가 입력한 height, width 받기
            height = self.connection.recv(1024)
            width = self.connection.recv(1024)
            print('height : ', height.decode())
            print('width : ', width.decode())

            # Convert과정 Byte -> String -> Int
            int_height = int(height.decode())
            int_width = int(width.decode())

            print('(', int_height, ',', int_width, ')')
            print("tcp server :: height, width data received!!")
           
            # Tcp protocol header 바이트 따로 추출
            buf = b''
            while len(buf)<4:
                buf += self.connection.recv(4-len(buf))
            size = struct.unpack('!i', buf)
            print("tcp server :: receiving %s bytes" % size)
            
            # Client에서 보낸 이미지 바이트 데이터 저장
            byte_image = b''
            while True:
                data = self.connection.recv(600000)
                if not data:
                    break
                byte_image += data
            print('tcp server :: image data received!!')
            print(len(byte_image))

            # 이미지 저장 과정
            try:
        
                print("tcp server :: saving received image...")
                image = Image.open(io.BytesIO(byte_image))
                #image = image.resize((int_width, int_height), Image.ANTIALIAS)
                print("tcp server :: saved image!!")
                image.save('testimg.bmp')
                #print("클라이언트에 전송 완료")

            except Exception as e:
                print(e)
            
            # -----딥러닝으로 이미지 파일 생성 중 ------
            # -----생성 완료-----

            print("---모델에서 생성된 이미지들 클라이언트로 전송 준비---")
            
            try:
                #if self.connection.recv(1024) == None  : # 클라이언트에서 데이터를 보내면 이미지 전송 시작
                print("tcp server :: ready to transfer images")
                filename_list = [102] # 전송할 이미지 수 만큼 배열 생성 
            
                file_count = len(filename_list)
                print("총 전송할 이미지 수 : ", file_count)
                #self.connection.send(b'%d' % file_count) # 이미지 파일이 총 몇개인지 클라이언트에 전송
                
                for i in filename_list:
                    deepGenerateImage = "C://Users//김규철//Desktop//imageData//수정//" + "img_c_" + str(i) + ".bmp" #img_c_101~105.bmp 이미지 가져오기
                    # 실제 활용 시에는 딥러닝 모델로 생성된 이미지 경로 넣기
                    file = open(deepGenerateImage, "rb")
                    img_size = os.path.getsize(deepGenerateImage) # 이미지 사이즈 저장
                    img = file.read(img_size) # img에 byte 배열 저장
                    print(img_size)
                    buff = b''
                    buff += (b'%d' % img_size)
                    print(buff)
                    self.connection.send(buff)
                    print(img_size, "전송 완료")
                    #print("전송 바이트 : ", img_size)
                    self.connection.sendall(img) # 클라이언트에 img 전송
                    file.close()
                    print("tcp server ::" + str(i) + " image transfer finish!")
                    #self.connection.send(b'*') # 클라이언트에게 파일의 끝을 알려주기 위해 '*' 전송
                    time.sleep(3) # 먼저 보낸 이미지 파일 모두 전송될 때까지 기다림
                #else :
                #    print("tcp server :: don't receive data")
                #    exit(0)
                print("tcp server :: transfer completed")
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