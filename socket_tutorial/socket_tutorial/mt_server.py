#多线程版本server
import socket

try:
    import _thread as thread #python 3中，将thread模块重命名为_thread
except ImportError:
    import dummy_thread as thread

import threading

def echo_server(address):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(10)
    while True:
        client, addr = sock.accept()
        print("connect from:" + str(addr))
        #thread.start_new_thread(client_handler, (client, )) #可以直接从函数开启线程
        #t = threading.Thread(target=client_handler, args=(client,), ) #传参数，注意 [,]
        t = client_thread(client) #也可以从线程对象开启
        t.setDaemon(True)
        
        t.start()
       
    
#处理客户端连接的回调（callback）
def client_handler(client):
    while True:
        try:
            data = client.recv(10000)
            client.send(str.encode("Got:") + data)
        except socket.error:
            print("close connection:" + str(client.getpeername()))
            client.close()
            thread.exit()
#处理客户端连接的线程类           
class client_thread(threading.Thread):
    def __init__(self, client):
        self.client = client
        return super().__init__()
    def run(self):
        while True:
            try:
                data = self.client.recv(10000)
                self.client.send(str.encode("Got:") + data)
            except socket.error:
                print("close connection:" + str(self.client.getpeername()))
                self.client.close()
                return

        

if __name__ == '__main__':
    echo_server(('', 3333))