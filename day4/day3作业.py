#!/usr/bin/env  python
# -*- coding:utf-8 -*-

def  fetch(backend):
    #backend  "www.oldboy.org"
    result = []
    with open('ha.conf','r',encoding='utf-8') as  f:
        flag = False

        for line in f:
            if line.strip() == "backend " + backend:
                flag = True
                continue
            if flag and line.strip().startswith("backend") == True:
                flag = False
                break
            if flag and len(line.strip()) != 0:
                result.append(line.strip())
    return result

def add(backend,record):
    #先检查记录是否存在
    record_list = fetch(backend) #如果record_list 的值为空，转换为bool值后，就是False
    if not record_list:        # 如果record_list 为False，那么not record_list 为True
        #backend不存在
        with open('ha.conf','r',encoding='utf-8') as old , open('new.conf','w',encoding='utf-8') as new:
            for line in old:
                new.write(line)
            new.write("\nbackend"+ backend + "\n")
            new.write(" " * 8 + record + "\n")

    else:  #backedn 存在
        if record in record_list:    #record 已经存在
            pass
        else:  #backend 存在，record不存在
            record_list.append(record)
            with open('ha.conf','r',encoding='utf-8') as old,open('new.conf','w',encoding='utf-8') as new:
                flag = False
                for line in old:
                    if line.strip().startswith("backend") and line.strip() == "backend" + backend:
                        flag = True
                        new.write(line)
                        for new_line in record_list:
                            new.write(" " * 8 + new_line + "\n")
                        continue
                    if flag and line.strip().startswith("backend"):
                        flag = False
                        new.write(line)
                        continue
                    if line.strip() and not flag:
                        new.write(line)


# ret = fetch("www.oldboy.org")
# print(ret)

bk = "www.oldboy.org"
rd = "server 100.1.7.99 100.1.7.99 weight 20 maxconn 30"
add(bk,rd)
