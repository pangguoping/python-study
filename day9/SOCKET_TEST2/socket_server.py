#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther: pangguoping

import socket
import subprocess
ip_port=('127.0.0.1',9990)
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
            p=subprocess.Popen(str(recv_data,encoding='utf-8'),shell=True,stdout=subprocess.PIPE)
            res=p.stdout.read()
            if len(res) == 0:
                send_data='cmd err'
            else:
                send_data=str(res,encoding='gbk')
            print(send_data)
            conn.send(bytes(send_data,encoding='utf-8'))

        except Exception:
            break
    #挂电话
    conn.close()
