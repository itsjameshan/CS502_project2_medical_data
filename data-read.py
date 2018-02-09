# read from any kafka
# write to any cassandra

import argparse
import logging
import json
import atexit

from cassandra.cluster import Cluster
from kafka import KafkaConsumer

topic_name = ''
kafka_broker = ''
cassandra_broker = ''
keyspace = ''
table = ''

logging.basicConfig()
logger = logging.getLogger('data-storage')
logger.setLevel(logging.DEBUG)

def save_data(stock_data, session):
	try:
		logger.debug('start to save data %s', stock_data)
		parsed = json.loads(stock_data)
		symbol = parsed.get('symbol')
		price = float(parsed.get('price'))
		timestamp = parsed.get('last_trade_time')

		statement = "INSERT INTO %s (symbol, trade_time, price) VALUES ('%s','%s',%f)" %(table, symbol,timestamp,price)
		session.execute(statement)
		logger.info('saved data into cassandra %s', stock_data)

	except Exception as e:
		logger.error('cannot save data %s', stock_data)

def shutdown_hook(consumer):
	logger.info('closing resource')
	consumer.close()
	#session.shutdown()
	logger.info('released resource')

if __name__ == '__main__':
	#setup command line argument

	parser = argparse.ArgumentParser()
	parser.add_argument('topic_name', help='the kafka topic name to subscribe from')
	parser.add_argument('kafka_broker', help= 'the kafka broker address')
	#parser.add_argument('cassandra_broker', help= 'the cassandra borker location')
	#parser.add_argument('keyspace', help= 'the keyspace')
	#parser.add_argument('table', help= 'the table in cassandra')

	# -parse argument
	args = parser.parse_args()
	topic_name = args.topic_name
	kafka_broker = args.kafka_broker
	#cassandra_broker = args.cassandra_broker
	#keyspace = args.keyspace
	#table = args.table

	# create kafka consumer
	consumer = KafkaConsumer(
		topic_name,
		bootstrap_servers = kafka_broker
	)

	atexit.register(shutdown_hook, consumer)

	for msg in consumer:
		logger.debug(msg)
		#save_data(msg.value, session)

