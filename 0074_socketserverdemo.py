#! /usr/bin/env python
# -*- coding: utf-8 -*-
# create by oldman
# Date: 2019/8/23
import socket
import threading
import time

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


