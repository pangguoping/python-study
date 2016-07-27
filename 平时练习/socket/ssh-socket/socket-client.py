#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther: pangguoping
"""


import socket
ip_port = ('127.0.0.1',9999)
#买手机
s = socket.socket()
#拨号
s.connect(ip_port)
#发送消息
send_data = input(">>>:").strip()
s.send(bytes(send_data,encoding='utf-8'))
#收消息
recv_data = s.recv(1024)
print("----------------",type(recv_data))
print(str(recv_data,encoding='utf-8'))
#挂电话
s.close()

"""
'''

#循环输入，exit退出，可以输入空字符
import socket
ip_port = ('127.0.0.1',9999)
#买手机
s = socket.socket()
#拨号
s.connect(ip_port)
#发送消息
while True:
    send_data = input(">>>:").strip()
    if len(send_data) == 0: continue   #如果输入是空字符，退出本次循环，继续下次循环
    s.send(bytes(send_data,encoding='utf-8'))
    if send_data == 'exit':break       #输入exit 退出程序
    #收消息
    recv_data = s.recv(1024)
    print("----------------",type(recv_data))
    print(str(recv_data,encoding='utf-8'))
#挂电话
s.close()
'''
'''
#循环输入，exit退出，可以输入空字符
import socket
ip_port = ('127.0.0.1',9999)
#买手机
s = socket.socket()
#拨号
s.connect(ip_port)
#发送消息
while True:
    send_data = input(">>>:").strip()
    if send_data == 'exit': break  # 输入exit 退出程序
    if len(send_data) == 0: continue   #如果输入是空字符，退出本次循环，继续下次循环
    s.send(bytes(send_data,encoding='utf-8'))

    #收消息
    recv_data = s.recv(1024)
    print("----------------",type(recv_data))
    print(str(recv_data,encoding='utf-8'))
#挂电话
s.close()
'''
#一个客户端断开连接后，服务端还可以接受新的连接
import socket
ip_port = ('127.0.0.1',9999)
#买手机
s = socket.socket()
#拨号

s.connect(ip_port)
#发送消息
while True:
    send_data = input(">>>:").strip()
    if send_data == 'exit': break  # 输入exit 退出程序
    if len(send_data) == 0: continue   #如果输入是空字符，退出本次循环，继续下次循环
    s.send(bytes(send_data,encoding='utf-8'))

    #收消息
    #解决粘包的问题
    ready_tag = s.recv(1024) # Ready|9999
    ready_tag = str(ready_tag,encoding='utf-8')
    if ready_tag.startswith('Ready'):  # Ready|9999
        msg_size = int(ready_tag.split('|')[-1])
    start_tag = 'Start'
    s.send(bytes(start_tag,encoding='utf-8')) #给server发送Start,告诉server可以准备发送数据了
    recv_size = 0  #初始化数据大小
    recv_msg =b''

    while recv_size < msg_size:
        recv_data = s.recv(1024)
        recv_msg += recv_data
        recv_size += len(recv_data)
        print('MSG SIZE %s RECE SIZE %s' % (msg_size, recv_size))

    print(str(recv_msg,encoding='utf-8'))
#挂电话
s.close()