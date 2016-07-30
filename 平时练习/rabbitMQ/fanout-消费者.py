#!/usr/bin/env python
# -*- coding: utf-8 -*-
# auth : pangguoping

#  rabbitmq 订阅者
import pika

credentials = pika.PlainCredentials('admin', 'admin')
#链接rabbit服务器（localhost是本机，如果是其他服务器请修改为ip地址）
connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.1.103',5672,'/',credentials))
channel = connection.channel()

# 定义交换机，进行exchange声明，exchange表示交换机名称，type表示类型
channel.exchange_declare(exchange='logs_fanout',
                         type='fanout')

# 随机创建队列
result = channel.queue_declare(exclusive=True)  # exclusive=True表示建立临时队列，当consumer关闭后，该队列就会被删除
queue_name = result.method.queue
# 将队列与exchange进行绑定
channel.queue_bind(exchange='logs_fanout',
                   queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] %r" % body)


# 从队列获取信息
channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()