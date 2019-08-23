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


def  client2():
    """
    半双工实现
    :return:
    """
    host = '127.0.0.1'
    port = 50001
    busize = 1024
    addr = (host, port)
    tryCon = 0

    tcps = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while True:
        try:
            tcps.connect(addr)
        except:
            print(u'正在尝试连接远程主机')

            tryCon +=1
            if tryCon ==3:
                print(u"无法连接上远程主机，请稍后再试")
                exit()
        else:
            break
    print(u"登录成功(通讯结束请输入'quiet'退出)\n")
    try:
        while True:
            data = str(input('> '))
            if not data:
                continue
            elif data=='quit':
                tcps.send(data)
                break
            else:
                tcps.send(data)


            while True:
                data = tcps.recv(busize)
                if not data:
                    continue
                else:
                    print(data)
                    break

    except socket.error as e:
        print("session closing")
        print(e)
    tcps.close()

client2()