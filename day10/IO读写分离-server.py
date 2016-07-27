#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther: pangguoping
#IO多路复用
import socket
import select

sk = socket.socket()
sk.bind(('127.0.0.1',9999))
sk.listen(5)
inputs = [sk,]
outputs = []
messages = {}
while True:
    rlist,wlist,e = select.select(inputs,outputs,[],1)
    #[sk,]表示要监听的socket的对象，只要有变化就写到rlist变量里。参数1表示超时时间
    #如果有新连接来了 rlist = [sk]，如果没有新连接过来，那么rlist会继续等待，此时rlist=[] 空列表
    #rlist中获取的就是socket对象列表
    #监听sk(服务端)对象，如果sk对象发生变化，表示有客户端来连接了，此时rlist值为sk
    #监听conn对象，如果conn发生变化，表示客户端有新消息发送过来了，此时rlist的值为【客户端】
    print(len(inputs),len(rlist),len(wlist),len(outputs))
    for r in rlist:
        if r == sk:
            #新客户来连接了
            print(r)
            conn,address = r.accept()
            #conn是什么？ 其实是socket对象
            inputs.append(conn)
            messages[conn] = []
            conn.sendall(bytes('hello',encoding='utf-8'))
        else:
            #有人给我发消息了
            print('===============')
            try:
                ret = r.recv(1024)
                if not ret:
                    raise Exception('断开连接')
                else:
                    outputs.append(r)
                    messages[r].append(ret)

            except Exception as e:
                inputs.remove(r)
                del messages[r]
    #所有给我发过消息的人
    for w in wlist:
        msg = messages[w].pop()
        resp = msg + bytes('response',encoding='utf-8')
        w.sendall(resp)
        outputs.remove(w)



