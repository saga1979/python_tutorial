import selectors
import socket

sel = selectors.DefaultSelector()

def accept(sock, mask):
    conn, addr = sock.accept()  
    print('accepted', conn, 'from', addr)
    conn.setblocking(False) #设置为非阻塞
    sel.register(conn, selectors.EVENT_READ, read)

def read(conn, mask):
    try:
        data = conn.recv(1000) 
        if data:
            print('echoing', repr(data), 'to', conn)
            conn.send(data)  
        else:
            print('closing', conn)
            sel.unregister(conn)
            conn.close()
    except ConnectionResetError :
        conn.close()
        sel.unregister(conn) #如果发生错误，关闭并从选择器中注销该连接

sock = socket.socket()
sock.bind(('localhost', 3333))
sock.listen(100)
sock.setblocking(False)
sel.register(sock, selectors.EVENT_READ, accept)

while True:
    events = sel.select()
    for key, mask in events:
        callback = key.data
        callback(key.fileobj, mask)