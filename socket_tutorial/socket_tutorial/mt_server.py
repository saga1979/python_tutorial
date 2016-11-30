import socket

try:
    import thread
except ImportError:
    import dummy_thread as thread

def echo_server(address):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(10)
    while True:
        client, addr = sock.accept()
        print("connect from:" + str(addr))
        thread.start_new_thread(client_handler, (client, ))

def client_handler(client):
    while True:
        try:
            data = client.recv(10000)
            client.send(str.encode("Got:") + data)
        except socket.error:
            print("close connection:" + str(client.getpeername()))
            client.close()
            thread.exit()

if __name__ == '__main__':
    echo_server(('', 3333))