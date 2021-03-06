#!/usr/bin/env python
# -*- coding: utf-8 -*-
# auth : pangguoping

import contextlib
import socket

@contextlib.contextmanager
def context_socket(host,port):
    sk = socket.socket()
    sk.bind((host,port))
    sk.listen(5)

    try:
        yield sk
    finally:
        sk.close()

with context_socket('127.0.0.1',8888) as sock:
    print(sock)