#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther: pangguoping

import socket

ip_port = ('127.0.0.1',8090)
sk = socket.socket()
sk.connect(ip_port)
sk.settimeout(5)

while True:
    data = sk.recv(1024)
    print('recive:',data.decode())  #相当于print('recive:',data,encoding='utf-8')
    inp = input('please input:')
    sk.sendall(bytes(inp,encoding='utf-8'))
    if inp == 'exit':
        break

sk.close()
