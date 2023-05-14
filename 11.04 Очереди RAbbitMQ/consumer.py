#!/usr/bin/env python3
# coding=utf-8
import pika

credentials = pika.PlainCredentials('artem','1006')
parameters = pika.ConnectionParameters('192.168.122.222',5672,'/', credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.queue_declare(queue='hello')
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
channel.basic_consume(queue='hello', on_message_callback=callback,auto_ack=True)
channel.start_consuming()
