#!/usr/bin/env python
# -*- coding: utf-8 -*-
# auth : pangguoping
#exchange 生产者
import pika
credentials = pika.PlainCredentials('admin', 'admin')
connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.11.123',5672,'/',credentials))
channel = connection.channel()
channel.exchange_declare(exchange='logs_fanout',type='fanout')
#随机创建队列
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue
#绑定
channel.queue_bind(exchange='logs_fanout',queue=queue_name)
print('[*] waiting for logs.To exit')
def callback(ch,method,properties,body):
    print('[x] %r' %body)

channel.basic_consume(callback,queue=queue_name,no_ack=True)
channel.start_consuming()
