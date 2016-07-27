#!/usr/bin/env python
# -*- coding: utf-8 -*-
# auth : pangguoping

#ftp 上传
import socket
import os
import json

ip_port = ('127.0.0.1',8010)
sk = socket.socket()
sk.connect(ip_port)
welcome_msg = sk.recv(1024)
print("from server:",welcome_msg.decode())

while True:
    send_data = input(">>>:").strip()
    if len(send_data) == 0:continue
    cmd_list = send_data.split()
    if len(cmd_list) < 2:continue
    task_type = cmd_list[0]
    if task_type == 'put':
        abs_filepath = cmd_list[1]
        if os.path.isfile(abs_filepath):
            file_size = os.stat(abs_filepath).st_size
            filename = abs_filepath.split('/')[-1]
            print('file:%s size:%s' %(abs_filepath,file_size))
            msg_data = {"action":"put",
                        "filename":filename,
                        "file_size":file_size}

            sk.send(bytes(json.dumps(msg_data),encoding='utf-8'))
            server_confirmation_msg = sk.recv(1024) #解决粘包问题
            confirm_data = json.loads(server_confirmation_msg.decode())
            if confirm_data['status'] == 200:

                print('start sending file',filename)
                f = open(abs_filepath,'rb')
                for line in f:
                    sk.send(line)
                print('send file done')

        else:
            print("\033[31;1mfile [%s] is not exist\033[0m" %abs_filepath)
            continue

    else:
        print('do not support task type',task_type)
        continue

    #sk.send(bytes(send_data,encoding='utf-8'))
    #收消息
    recv_data = sk.recv(1024)
    print(str(recv_data,encoding='utf-8'))

sk.close()
