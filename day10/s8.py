#!/usr/bin/env python
# -*- coding: utf-8 -*-
# auth : pangguoping

import socketserver

class MyClass(socketserver.BaseRequestHandler):
    def handle(self):
        pass
obj = socketserver.ThreadingTCPServer(('127.0.0.1',9999),MyClass)
obj.serve_forever()