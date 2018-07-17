#!/usr/bin/python
import argparse
import pika
import sys
import logging

def print_data(channel, method, properties, body):
    print 'body:', body

__author__ = 'humsterman86'

parser = argparse.ArgumentParser(description='Simple utility for RabbitMQ management')
parser.add_argument('-q','--queue', help='Get queue messages by name', required=True)

args = parser.parse_args()

if args.queue:
    try:
	parameters = pika.ConnectionParameters('localhost')
	connection = pika.BlockingConnection(parameters)
	channel = connection.channel()
	if (channel.queue_declare(queue=args.queue, exclusive=False,auto_delete=False, passive=True)):
	    channel.basic_consume(print_data, queue=args.queue)
	    channel.start_consuming()
	    connection.close()
    except:
	print ("Wrong queue name - 404 Not found")