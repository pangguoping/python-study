#!/usr/bin/env python
# -*- coding: utf-8 -*-
# auth : pangguoping
# rabbitmq 发布者
import pika

credentials = pika.PlainCredentials('admin', 'admin')
#链接rabbit服务器（localhost是本机，如果是其他服务器请修改为ip地址）
connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.1.103',5672,'/',credentials))
channel = connection.channel()
# 定义交换机，exchange表示交换机名称，type表示类型
channel.exchange_declare(exchange='logs_fanout',
                         type='fanout')

message = 'Hello Python'
# 将消息发送到交换机
channel.basic_publish(exchange='logs_fanout',  # 指定exchange
                      routing_key='',  # fanout下不需要配置，配置了也不会生效
                      body=message)
print(" [x] Sent %r" % message)
connection.close()