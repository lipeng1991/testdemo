#! /usr/bin/env python
# -*- coding: utf-8 -*-
# create by oldman
# Date: 2019/8/23
import socket

def client1():
    """
    socket编程单向client端
    :return:
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 建立连接
    s.connect(('127.0.0.1', 9999))
    print(s.recv(1024))
    for d in ["John", "Tracy", "Sarah"]:
        s.send(d)
        print(s.recv(1024))

    s.send('exit')
    s.close()