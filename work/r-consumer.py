#!/usr/bin/env python
# -*- coding: utf-8 -*-
# auth : pangguoping
import pika
credentials = pika.PlainCredentials('admin', 'admin')
connection = pika.BlockingConnection(pika.ConnectionParameters('dev-api-node2',56720,'/',credentials))
channel = connection.channel()
channel.queue_declare(queue='hello', durable=True)
def callback(ch,method,properties,body):
    print("[x] Received %r" %body)

channel.basic_consume(callback,queue='hello',no_ack=True)
print('[*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()