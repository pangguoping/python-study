#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther: pangguoping
"""


import socket
import subprocess
ip_port=('127.0.0.1',9999)
s=socket.socket()
s.bind(ip_port)
s.listen(5)
while True:
    conn,addr=s.accept()
    while True:
        try:
            recv_data=conn.recv(1024)
            if len(recv_data) == 0:break
            p=subprocess.Popen(str(recv_data,encoding='utf-8'),shell=True,stdout=subprocess.PIPE)
            res=p.stdout.read()
            if len(res) == 0:
                send_data = 'cmd err'
            else:
                send_data=str(res,encoding='gbk')
            #解决粘包问题
                ready_tag='Ready|%s' %len(send_data)
                conn.send(bytes(ready_tag,encoding='utf-8'))
                feedback=conn.recv(1024)
                feedback=str(feedback,encoding='utf-8')
                if feedback.startswith('Start'):
                    conn.send(send_data)
        except Exception:
            break

    conn.closed()

    """
"""

import socket
ip_port=('127.0.0.1',9999)
#买手机
s = socket.socket()
#买手机卡
s.bind(ip_port)
#开机
s.listen(5)
#等待电话
conn,addr = s.accept()
#conn 相当于一条通信线路
#收消息
recv_data = conn.recv(1024)
print("----------------",type(recv_data))
#发消息
send_data = recv_data.upper()
conn.send(send_data)
#挂电话
conn.close()

"""
'''

#循环输入，exit退出，可以输入空字符
import socket
ip_port=('127.0.0.1',9999)
#买手机
s = socket.socket()
#买手机卡
s.bind(ip_port)
#开机
s.listen(5)
#等待电话
conn,addr = s.accept()
#conn 相当于一条通信线路
#收消息
while True:
    try:
        recv_data = conn.recv(1024)
        print("----------------",type(recv_data))
        if str(recv_data,encoding='utf-8') == 'exit': break
        #发消息
        send_data = recv_data.upper()
        conn.send(send_data)
    except Exception:
        break
#挂电话
conn.close()
'''
'''
#循环输入，exit退出，可以输入空字符
import socket
ip_port=('127.0.0.1',9999)
#买手机
s = socket.socket()
#买手机卡
s.bind(ip_port)
#开机
s.listen(5)
#等待电话
conn,addr = s.accept()
#conn 相当于一条通信线路
#收消息
while True:
    recv_data = conn.recv(1024)
    if len(recv_data) == 0:break
    #发消息
    send_data = recv_data.upper()
    conn.send(send_data)

#挂电话
conn.close()
'''

#一个客户端断开连接后，服务端还可以接受新的连接
import socket
import subprocess
ip_port=('127.0.0.1',9999)
#买手机
s = socket.socket()
#买手机卡
s.bind(ip_port)
#开机
s.listen(2)
#等待电话
while True:
    conn,addr = s.accept()
    #conn 相当于一条通信线路
    #收消息
    while True:
        try:  #客户端强制断开（不是输入exit） 会出现异常。
            recv_data = conn.recv(1024)
            if len(recv_data) == 0:break
            #发消息
            p=subprocess.Popen(str(recv_data,encoding='utf-8'),shell=True,stdout=subprocess.PIPE)
            res = p.stdout.read()
            if len(res) == 0:   #处理输入的错误命令
                send_data = 'cmd err'
            else:
                send_data = str(res,encoding='gbk')   #windows平台下解码成gbk,并且gbk转换为str
            #解决粘包问题
            send_data = bytes(send_data,encoding='utf-8')  #编码成utf-8,字节,并把str转换为字节
            ready_tag = 'Ready|%s' %len(send_data)
            conn.send(bytes(ready_tag,encoding='utf-8'))
            feedback = conn.recv(1024)  #收到客户端发送过来的Start
            feedback = str(feedback,encoding='utf-8')  #把收到的feedback 转换为str
            if feedback.startswith('Start'):
                conn.send(send_data)
        except Exception:
            break
    #挂电话
    conn.close()



















