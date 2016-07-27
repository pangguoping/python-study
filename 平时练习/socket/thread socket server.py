#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther: pangguoping
import socketserver

class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        #print self.request , self.client_address,self.server
        conn = self.request
        conn.sendall(bytes('欢迎致电10086,请输入1xxx,0转人工服务',encoding='utf-8'))
        Flag = True
        while Flag:
            data = conn.recv(1024)
            print(str(data.decode()))
            if str(data.decode()) == 'exit':
                Flag = False
            elif str(data.decode()) == '0':
                conn.sendall(bytes('通过可能会被录音',encoding='utf-8'))
            else:
                conn.sendall(bytes('请重新输入',encoding='utf-8'))

if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1',8090),MyServer)
    server.serve_forever()