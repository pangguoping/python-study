#!/usr/bin/env python
# -*- coding: utf-8 -*-
# auth : pangguoping

'''


import paramiko



# 创建SSH对象
ssh = paramiko.SSHClient()
# 允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接服务器
ssh.connect(hostname='192.168.11.139', port=22, username='root', password='123')

# 执行命令
stdin, stdout, stderr = ssh.exec_command('ifconfig')
# 获取命令结果
result = stdout.read()
print(result)

# 关闭连接
ssh.close()
'''
import paramiko

import uuid

class SSHConnection(object):

    def __init__(self, host='192.168.11.139', port=22, username='root',pwd='123'):
        self.host = host
        self.port = port
        self.username = username
        self.pwd = pwd
        self.__k = None

    def run(self):
        self.connect()
        pass
        self.close()

    def connect(self):
        transport = paramiko.Transport((self.host,self.port))
        transport.connect(username=self.username,password=self.pwd)
        self.__transport = transport

    def close(self):
        self.__transport.close()

    def cmd(self, command):
        ssh = paramiko.SSHClient()
        ssh._transport = self.__transport
        # 执行命令
        stdin, stdout, stderr = ssh.exec_command(command)
        # 获取命令结果
        result = stdout.read()
        return result

    def upload(self,local_path, target_path):
        # 连接，上传
        sftp = paramiko.SFTPClient.from_transport(self.__transport)
        # 将location.py 上传至服务器 /tmp/test.py
        sftp.put(local_path, target_path)

ssh = SSHConnection()
ssh.connect()

r1 = ssh.cmd('ls && df -h')
print(r1.decode())

#ssh.upload('s2.py', "/home/alex/s7.py")

ssh.close()
