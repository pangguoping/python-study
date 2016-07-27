#!/usr/bin/env python
# -*- coding: utf-8 -*-
# auth : pangguoping
import pika

# ##########生产者 ###########
credentials = pika.PlainCredentials('admin', 'admin')
connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.11.123',5672,'/',credentials))
channel = connection.channel()

channel.queue_declare(queue='hello')
channel.basic_publish(exchange='',routing_key='hello',body='Hello World!')
print("[x] Sent 'Hello World'")
connection.close()