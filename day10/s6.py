#!/usr/bin/env python
# -*- coding: utf-8 -*-
# auth : pangguoping
'''


import socket
import select

sk = socket.socket()
sk.bind(('127.0.0.1',9990,))
sk.listen(5)

while True:
    rlist,w,e = select.select([sk,],[],[],1)
    #监听sk(服务端)对象,如果sk对象发生变化,表示有客户端来连接了,此时rlist值为【sk】
    #监听conn对象,如果conn发生变化,表示客户端有新消息发送过来了,此时rlist的值为【客户端】
    #print(rlist)
    #rlist 中socket对象列表,[sk,]
    for r in rlist:
        print(r)
        conn,address = r.accept()
        conn.sendall(bytes('hello',encoding='utf-8'))
#rlist = [sk,],rlist=[sk1,],rlist = [sk1,sk2]
#rlist = []
'''

'''

import socket
import select
sk = socket.socket()
sk.bind(('127.0.0.1',9999,))
inputs=[sk,]
while True:
    rlist,w,e = select.select(inputs,[],[],1)
    print(len(inputs),len(rlist))

    for r in rlist:
        if r == sk:
            conn,address = r.accept()
            inputs.append(conn)
            conn.sendall(bytes('hello',encoding='utf-8'))
        else:
            print('=======')
            r.recv(1024)

'''

#实现读写分离
import socket
import select
sk = socket.socket()
sk.bind(('127.0.0.1',9999,))
inputs=[sk,]
outputs = []
while True:
    rlist,wlist,e, = select.select(inputs,outputs,[],1)
    print(len(inputs),len(rlist),len(wlist),len(outputs))

    for r in rlist:
        if r == sk:
            conn,address = r.accept()
            inputs.append(conn)
            conn.sendall(bytes('hello',encoding='utf-8'))
        else:
            #有人给我发消息了
            print('=======')
            try:
                ret = r.recv(1024)
                if not ret:
                    raise Exception('断开连接')
                else:
                    outputs.append(r)
            except Exception as e:
                inputs.remove(r)
    #所有给我发过消息的人
    for w in wlist:
        w.sendall(bytes('response',encoding='utf-8'))
        outputs.remove(w)


