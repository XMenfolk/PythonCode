# coding=utf-8

import time
import socket
import threading

# 创建一个基于 IPv4 和 TCP 协议的 Socket：
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定监听的地址和端口：
s.bind(('127.0.0.1', 9999))

# 监听端口，传入的参数指定等待连接的最大数量：
s.listen(5)
print 'Waiting for connection...'

# 通过一个永久循环来接受来自客户端的连接， accept() 会等待并返回一个客户端的连接:
while True:
    # 接收一个新连接：
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接：
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()


# 每个连接都必须创建新线程（或进程）来处理，否则，单线程在处理连接的过程中，无法接受其他客户端的连接：
def tcplink(sock, addr):
    print 'Accept new connection from %s:%s...' % addr
    sock.send('Welcome!')


    # 连接建立后，服务器首先发一条欢迎消息，然后等待客户端数据，并加上 Hello 再发送给客户端。如果客户端发送了 exit 字符串，就直接关闭连接

    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if data == 'exit' or not data:
            break
        sock.send('Hello,%s!' % data)
    sock.close()
    print 'Connection from %s:%s closed.' % addr

