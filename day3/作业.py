#!/usr/bin/env  python
# -*- coding:utf-8 -*-
# pangguoping
import json
import os
import time
time_flag=time.strftime('%Y-%m-%d-%H-%M-%S')
def search(backend):
    """
    :param backend:用户输入的域名
    :return: result_list  返回查询到的结果，列表形式
    """
    result_list = []  #设置查询结果的空列表
    backend_title = 'backend %s' % backend
    with open('haproxy.conf','r+',encoding="utf-8")  as haproxy_read:
        flag = False  #设置初始标记符

        for line in haproxy_read.readlines():

            line = line.strip()  #每一行去掉两端的空格
            #print(line)
            if line == backend_title:  #判断输入和文件中是否匹配
                flag = True   #修改标记符
                continue     #跳出本次循环，继续下次循环
            if flag == True and line.startswith('backend'):  #确认是否为下一个backend标记
                flag = False   #修改标记符
                break     #退出整个循环
            if flag == True and len(line)!=0:  #查询到backend，而且下面的server记录也不为空
                result_list.append(line)  # 把查询到的结果追加到列表中
                #print(result_list)
    return result_list   #返回列表内容


def add(dict_info):
    backend = dict_info.get('backend')
    #print(backend)
    record_list = search(backend)
    #print(record_list)
    backend_title = "backend %s" %backend
    server = dict_info['record']['server']
    weight = dict_info['record']['weight']
    maxconn = dict_info['record']['maxconn']
    #current_record = "server %s %s weight %d maxconn %d" % (dict_info['record']['server'],dict_info['record']['server'],dict_info['record']['weight'],dict_info['record']['maxconn'])
    current_record = 'server %s %s weight %s maxconn %s' %(server,server,weight,maxconn)
    #print(dict_info['record']['server'],dict_info['record']['server'])
    #print(current_record)
    if len(record_list)==0:  #如果无对应域名记录，新增域名及对应的记录
        #print('record_list1 %s'%record_list)
        record_list.append(backend_title)
        record_list.append(current_record)
        with open('haproxy.conf','r') as read_file, open('haproxy.conf_new','w')  as write_file:
            flag = False
            for line in read_file:
                write_file.write(line)   #把haproxy.conf文件内容写入到haproxy.conf.new文件中
            for i in record_list:
                if i.startswith('backend'):
                    write_file.write(i+'\n')  #增加域名信息
                else:
                    write_file.write("%s%s\n" % (8*" ",i))   #增加域名对应的服务器信息
        #回显，提示用户无域名信息，将新增信息到配置文件最后
        print('No domain target,will add to the end of the "ha",has been add the end of file..')
        time.sleep(2)
        print('Information has been added successly!!!!')
        os.rename('haproxy.conf', 'haproxy.conf.bak.%s' % time_flag)  #备份原配置文件
        os.rename('haproxy.conf_new', 'haproxy.conf')  # 让新配置文件生效


    else:
        if current_record in record_list:  # 如果服务器信息重叠，提示用户信息已重叠，不操作文件
            print('\033[31;1mThe server info had been in %s domain,do not need to add...\033[0m' % current_record)
        else:
            record_list.insert(0,backend_title)  #把backend和域名添加到列表中
            if current_record not in record_list:
                record_list.append(current_record)
                print(record_list1:%s %record_list)
            with open('haproxy.conf','r') as read_file, open('haproxy.conf_new','w') as write_file:
                flag = False
                has_write = False
                for line in read_file:
                    line_strip = line.strip()
                    if line_strip == backend_title: #如果其中一行内容为“backend 域名”，更改标识符
                        flag = True
                        continue
                    if flag==True and line_strip.startswith('backend'):
                        flag = False
                    if not flag:
                        write_file.write(line)
                    else:
                        if not has_write:
                            for i in record_list:
                                if i.startswith('backend'):
                                    write_file.write(i+'\n')   #添加backend 和域名
                                else:
                                    write_file.write("%s%s\n" % (8*" ",i))  #添加server记录
                        has_write = True
            print('Information has been added successly!!!!')
            os.rename('haproxy.conf', 'haproxy.conf.bak.%s' % time_flag)  #备份原配置文件
            os.rename('haproxy.conf_new', 'haproxy.conf')  # 让新配置文件生效








#定义主函数
def main():
    start_num = input("1.查询ha\n2.增加ha\nPlease input your num:")   #获取要操作的num
    if start_num == '1':
        search_info = input("Please input bakcend :")   #输入要操作的backend
        search_result = search(search_info)    #获取search_backend函数 返回的结果
        if search_result:   #如果返回的结果不为空，那么就打印结果
            for backend_server in search_result:
                print(backend_server)   #打印结果
        else:
            print("sorry,没有找到backend :%s"%search_info)   #如果结果为空，输出未找到
    elif start_num == '2':
        data = input("请输入要增加的内容 :")
        dict_data = json.loads(data)  #通过json模块，将字符串转化为字典
        #print(dict_data)
        add(dict_data)

#执行主函数
main()




