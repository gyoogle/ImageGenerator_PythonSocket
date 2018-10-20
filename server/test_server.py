import socket
import struct
address = ("", 4000)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(address)
s.listen(1000)


client, addr = s.accept()
print('got connected from', addr)

buf = b''
while len(buf)<4:
    buf += client.recv(4-len(buf))
size = struct.unpack('!i', buf)
print("receiving %s bytes" % size)

with open('tst1.jpg', 'wb') as img:
    while True:
        data = client.recv(1024)
        if not data:
            break
        img.write(data)
print('received, yay!')

client.close()