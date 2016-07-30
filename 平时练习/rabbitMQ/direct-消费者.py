#!/usr/bin/env python
# -*- coding: utf-8 -*-
# auth : pangguoping
# 发布者
import pika

credentials = pika.PlainCredentials('admin', 'admin')
#链接rabbit服务器（localhost是本机，如果是其他服务器请修改为ip地址）
connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.1.103',5672,'/',credentials))
channel = connection.channel()
# 定义交换机名称及类型
channel.exchange_declare(exchange='direct_test',
                         type='direct')

severity = 'info'
message = '123'
# 发布消息至交换机direct_test，且发布的消息携带的关键字routing_key是info
channel.basic_publish(exchange='direct_test',
                      routing_key=severity,
                      body=message)
print(" [x] Sent %r:%r" % (severity, message))
connection.close()