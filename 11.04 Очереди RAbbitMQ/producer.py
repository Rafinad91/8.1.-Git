#!/usr/bin/env python3
# coding=utf-8
import pika

credentials = pika.PlainCredentials('artem','1006')
parameters = pika.ConnectionParameters('192.168.122.138',5672,'/', credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.queue_declare(queue='Netology')
channel.basic_publish(exchange='hello', routing_key='hello', body='Hello Netology!')
print (" Hello Netology")
connection.close()
