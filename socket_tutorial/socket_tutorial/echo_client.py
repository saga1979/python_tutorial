import socket
import time
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

client.connect(("192.168.56.1", 3333))

while True:
    client.send(b"hello")
    
    msg = client.recv(1024)
    print(msg)
    time.sleep(1)