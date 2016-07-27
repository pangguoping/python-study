#!/usr/bin/env python
# -*- coding: utf-8 -*-
# auth : pangguoping

import pika
# 消费者
credentials = pika.PlainCredentials('admin', 'admin')
connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.11.123',5672,'/',credentials))
channel = connection.channel()
channel.queue_declare(queue='hello')
def callback(ch,method,properties,body):
    print("[x] Received %r" %body)

channel.basic_consume(callback,queue='hello',no_ack=True)
print('[*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()