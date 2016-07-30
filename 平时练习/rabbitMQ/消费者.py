#!/usr/bin/env python
# -*- coding: utf-8 -*-
# auth : pangguoping
'''



import pika

# ########################## 消费者 ##########################
credentials = pika.PlainCredentials('admin', 'admin')
# 连接到rabbitmq服务器
connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.1.103',5672,'/',credentials))
channel = connection.channel()

# 声明消息队列，消息将在这个队列中进行传递。如果队列不存在，则创建
channel.queue_declare(queue='wzg')


# 定义一个回调函数来处理，这边的回调函数就是将信息打印出来。
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


# 告诉rabbitmq使用callback来接收信息
channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)
 # no_ack=True表示在回调函数中不需要发送确认标识

print(' [*] Waiting for messages. To exit press CTRL+C')

# 开始接收信息，并进入阻塞状态，队列里有信息才会调用callback进行处理。按ctrl+c退出。
channel.start_consuming()
'''
import pika
credentials = pika.PlainCredentials('admin', 'admin')
# 链接rabbit
connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.1.103',5672,'/',credentials))
# 创建频道
channel = connection.channel()
# 如果生产者没有运行创建队列，那么消费者创建队列
channel.queue_declare(queue='hello')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    import time
    time.sleep(10)
    print
    'ok'
    ch.basic_ack(delivery_tag=method.delivery_tag)  # 主要使用此代码


channel.basic_consume(callback,
                      queue='hello',
                      no_ack=False)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()