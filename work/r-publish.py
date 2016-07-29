#!/usr/bin/env python
# -*- coding: utf-8 -*-
# auth : pangguoping

import pika
credentials = pika.PlainCredentials('admin', 'admin')
connection = pika.BlockingConnection(pika.ConnectionParameters('dev-api-node2',5672,'/',credentials))
channel = connection.channel()

channel.queue_declare(queue='hello2', durable=True)  #队列持久化
#channel.queue_declare(queue='hello')
channel.basic_publish(exchange='',routing_key='hello2',body='Hello World!',properties=pika.BasicProperties(delivery_mode = 2,))
#channel.basic_publish(exchange='',routing_key='hello',body='Hello World!')

print("[x] Sent 'Hello World'")
connection.close()
