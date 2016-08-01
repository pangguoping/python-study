#!/usr/bin/env python
# -*- coding: utf-8 -*-
# auth : pangguoping

import paramiko
import sys
import os
import socket
import select
import getpass

tran = paramiko.Transport(('192.168.11.139', 22,))
tran.start_client()
tran.auth_password('oldboy', '123')

# 打开一个通道
chan = tran.open_session()
# 获取一个终端
chan.get_pty()
# 激活器
chan.invoke_shell()

while True:
    # 监视用户输入和服务器返回数据
    # sys.stdin 处理用户输入
    # chan 是之前创建的通道，用于接收服务器返回信息
    readable, writeable, error = select.select([chan, sys.stdin, ],[],[],1)
    if chan in readable:
        try:
            x = str(chan.recv(1024),encoding='utf-8')
            if len(x) == 0:
                print('\r\n*** EOF\r\n')
                break
            sys.stdout.write(x)
            sys.stdout.flush()
        except socket.timeout:
            pass
    if sys.stdin in readable:
        inp = sys.stdin.readline()
        chan.sendall(inp)

#########
# 利用sys.stdin,肆意妄为执行操作
# 用户在终端输入内容，并将内容发送至远程服务器
# 远程服务器执行命令，并将结果返回
# 用户终端显示内容
#########

chan.close()
tran.close()