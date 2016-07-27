#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther: pangguoping
import socket
ip_port = ('192.168.11.58',8009)
s = socket.socket()
s.connect(ip_port)
welcome_msg = s.recv(1024)
print("from server:",welcome_msg.decode())
while True:
    send_data = input(">>>:").strip()
    if len(send_data) == 0:continue
    s.send(bytes(send_data,encoding='utf-8'))
    recv_data = s.recv(1024)
    print(str(recv_data,encoding='utf-8'))
s.close()