#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther: pangguoping
import socketserver
class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        self.request.sendall(bytes('欢迎致电10086，请输入1xxx,0',encoding='utf-8'))
        while True:
            data = self.request.recv(1024)
            print("---->",len(data))
            if len(data) == 0:break

            print("[%s] says:%s" %(self.client_address,data.decode()))
            self.request.sendall(data.upper())

if __name__=='__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1',8009),MyServer)
    server.serve_forever()