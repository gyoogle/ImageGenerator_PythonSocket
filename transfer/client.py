import socket
import sys
import time

# 이미지 파일 저장경로
src = "C:\\Users\\김규철\\Desktop\\download\\"


def fileName():
    dte = time.localtime()
    Year = dte.tm_year
    Mon = dte.tm_mon
    Day = dte.tm_mday
    WDay = dte.tm_wday
    Hour = dte.tm_hour
    Min = dte.tm_min
    Sec = dte.tm_sec
    imgFileName = src + str(Year) + '_' + str(Mon) + '_' + str(Day) + '_' + str(Hour) + '_' + str(Min) + '_' + str(
        Sec) + '.bmp';
    return imgFileName


def save_img(data):
    img_fileName = fileName()
    img_file = open(img_fileName, "wb")
    print("finish img recv")
    print(sys.getsizeof(data))
    img_file.write(data)
    img_file.close()
    print("Finish ")


def receive_img():
    img_data = client_socket.recv(1024)
    data = img_data
    if img_data:
        while img_data:
            print("****************************recving Img...****************************")
            img_data = client_socket.recv(1000000)
            data += img_data
            save_img(data)
            if img_data[-1:] == b'*':
                break


# 서버 연결
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("172.20.10.6", 5000))
client_socket.send(b'hi')

file_count = client_socket.recv(1024)
print(file_count)
file_count = int(file_count)
print(file_count)
for i in range(file_count):
    receive_img()