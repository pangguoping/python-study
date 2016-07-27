#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther: pangguoping
"""

import socket
ip_port=('127.0.0.1',9999)
#买手机
s=socket.socket()
#买手机卡
s.bind(ip_port)
#开机
s.listen(5)
#等待电话
conn,addr=s.accept()
#收消息
recv_data=conn.recv(1024)
#发消息
send_data=recv_data.upper()
conn.send(send_data)
conn.close()

"""

import socket
ip_port=('127.0.0.1',9999)
#买手机
s=socket.socket()
s.bind(ip_port)
s.listen(5)
while True:
    conn,addr=s.accept()
    while True:
        try:
            recv_data=conn.recv(1024)
            if len(recv_data) == 0:break
            #发消息
            send_data=recv_data.upper()
            print(send_data)
            conn.send(send_data)
        except Exception:
            break
    #挂电话
    conn.close()
