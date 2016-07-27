#!/usr/bin/env python
# -*- coding: utf-8 -*-
# auth : pangguoping

#ftp server 上传文件
import socketserver
import json

class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        #print self.request,self.client_address,self.server
        conn = self.request
        conn.sendall(bytes('欢迎您的到来!',encoding='utf-8'))
        while True:
            data = conn.recv(1024)
            if len(data) == 0:break
            print("[%s] says:%s" % (self.client_address,data.decode()))
            #[('127.0.0.1', 51852)]  says:{"file_size": 1670262, "filename": "IMG_20160714_172632.jpg", "action": "put"}
            task_data = json.loads(str(data,encoding='utf-8'))
            task_action = task_data.get("action")
            if hasattr(self,"task_%s" %task_action):
                func = getattr(self,"task_%s" %task_action)
                func(task_data)
            else:
                print("task action is not supported",task_action)


    def task_put(self,*args,**kwargs):
        print("put",args,kwargs)
        #put ({'file_size': 1670262, 'action': 'put', 'filename': 'IMG_20160714_172632.jpg'},) {}
        file_size = args[0].get('file_size')
        file_name = args[0].get('filename')
        server_response = {"status":200} #解决粘包问题
        self.request.send(bytes(json.dumps(server_response),encoding='utf-8'))
        f = open(file_name,'wb')
        recv_size = 0
        while recv_size < file_size:
            data = self.request.recv(4096)
            f.write(data)
            recv_size += len(data)
            print('filesize: %s recvsize:%s' %(file_size,recv_size))
        print('file reve success')
        f.close()





if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1',8010),MyServer)
    server.serve_forever()














