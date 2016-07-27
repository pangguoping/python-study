#!/usr/bin/env python
# -*- coding: utf-8 -*-
# auth : pangguoping
'''
import socket

sk = socket.socket()
sk.connect(("127.0.0.1",9990,))
data = sk.recv(1024)
print(data)
while True:
    input(">>>>:")
sk.close()
'''
'''
import socket
sk = socket.socket()
sk.connet(('127.0.0.1',9999))
dat = sk.recv(1024)
print(data)
while True:
    inp = input(">>>>:")
    sk.sendall(bytes(inp,encoding='utf-8'))
sk.close()
'''
#实现读写分离
import socket

sk = socket.socket()
sk.connect(("127.0.0.1",9999,))
data = sk.recv(1024)
print(data)
while True:
    inp = input(">>>>:")
    sk.sendall(bytes(inp,encoding='utf-8'))
    print(sk.recv(1024))
sk.close()




















