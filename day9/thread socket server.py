#!/usr/bin/env python
# -*- coding: utf-8 -*-
# auth : pangguoping

#socketserver  实现多并发命令执行
import socketserver
import subprocess

class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        #print self.request,self.client_address,self.server
        conn = self.request
        conn.sendall(bytes('欢迎您的到来!',encoding='utf-8'))
        while True:
            data = conn.recv(1024)
            print("--->",len(data))
            if len(data) == 0:break
            print("[%s] says:%s" % (self.client_address,data.decode()))

            cmd = subprocess.Popen(data.decode(),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            cmd_res = cmd.stdout.read()
            if not cmd_res:
                cmd_res = cmd.stderr.read()
            if len(cmd_res) == 0: # cmd has not output
                cmd_res = bytes('cmd has output',encoding='utf-8')
            #解决粘包问题
            ready_tag = 'Ready|%s' %len(cmd_res)
            conn.send(bytes(ready_tag,encoding='utf-8'))
            feedback = conn.recv(1024)    #收到客户端发送过来的Start
            feedback = str(feedback,encoding='utf-8')  #把收到的feedback转换为str
            if feedback.startswith('Start'):
                conn.send(cmd_res)

if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1',8070),MyServer)
    server.serve_forever()














