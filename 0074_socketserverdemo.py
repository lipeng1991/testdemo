#! /usr/bin/env python
# -*- coding: utf-8 -*-
# create by oldman
# Date: 2019/8/23
import socket
import threading
import time

from pip._vendor.distlib.compat import raw_input

"""
1.单工版非常简单，只能客户端单方面向服务端发消息，服务端回复固定模板消息。
2. 半双工实现是连接建立以后，服务器等待客户端发送消息，客户端发送消息后等待接收服务器，这样一来一回循环往复下去。直到出现quit，关闭连接。


"""
def server01():
    """
    socket编程单向server端
    :return:
    """
    def tcplink(sock, addr):
        print('Access new connection from {}'.format(addr))
        sock.send('Welcome!')
        while True:
            data = sock.recv(1024)
            print(data)
            time.sleep(1)
            if not data or data =='exit':
                break
            sock.send('Hello, {}'.format(addr))


    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.bind(('127.0.0.1', 9999))
    s.listen(5)
    print('Waiting for connection....')
    while True:
        # 接受一个新连接
        sock, addr = s.accept()
        # 创建新线程来处理TCP连接
        t = threading.Thread(target=tcplink,args=(sock, addr))
        t.start()



def sercer02():
    """
    半双工实现
    :return:
    """
    host = '127.0.0.1'
    port = 50001
    busize = 1024
    addr = (host, port)

    def closetcnt(s):
        s.close()
        print("Session closing")

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(addr)
    s.listen(1)
    try:
        while True:
            print("waiting for connecting....")
            ts, caddr = s.accept()
            print("...connection from :{}".format(caddr))
            try:
                while True:
                    rdata = ts.recv(busize)
                    if not rdata:
                        continue
                    elif rdata == 'quit':
                        break
                    else:
                        print("from {}  {} \n {}".format(caddr[0], time.ctime(), rdata))
                    while True:
                        sdata = str(input('> '))
                        if not sdata:
                            break
                        else:
                            ts.send("from {}  {} \n {}".format(caddr[0], time.ctime(), sdata))
                            break

            except socket.error as  detail:
                print(detail)
            closetcnt(ts)

    finally:
        s.close

sercer02()