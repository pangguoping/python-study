#!/usr/bin/env python
# -*- coding: utf-8 -*-
# auth : pangguoping

import socket

ip_port = ('127.0.0.1',8070)
sk = socket.socket()
sk.connect(ip_port)
welcome_msg = sk.recv(1024)
print("from server:",welcome_msg.decode())
while True:
    send_data = input(">>>:").strip()
    if len(send_data) == 0:continue
    sk.send(bytes(send_data,encoding='utf-8'))
    #解决粘包的问题
    ready_tag = sk.recv(1024)  #收到的格式为  Ready|9999
    ready_tag = str(ready_tag,encoding='utf-8')
    if ready_tag.startswith('Ready'):
        msg_size = int(ready_tag.split('|')[-1])
    start_tag = 'Start'
    sk.send(bytes(start_tag,encoding='utf-8')) #给server发送Start,告诉server可以准备发送数据了
    recv_sise = 0  #初始化数据大小
    recv_msg = b''
    while recv_sise < msg_size: #解决粘包问题
        recv_data = sk.recv(1024)
        recv_msg += recv_data
        recv_sise += len(recv_data)
        print('MSG SIZE %s RECV SIZE %s' %(msg_size,recv_sise))
    print(str(recv_msg,encoding='utf-8'))

sk.close()
