#!/usr/bin/env python
# -*- coding: utf-8 -*-
# auth : pangguoping

import socketserver

class MyClass(socketserver.BaseRequestHandler):
    def handle(self):
        pass
#创建socket对象
#accept
#server_address = ('127.0.0.1',9999)
#RequestHandlerClass = MyClass == ()
#self.RequestHandlerClass() = MyClass() == ()
#1、obj封装了self.RequestHandlerClass = MyClass
#2、创建了socket,bind,listen

obj = socketserver.ThreadingTCPServer(('127.0.0.1',9999),MyClass)
obj.serve_forever()