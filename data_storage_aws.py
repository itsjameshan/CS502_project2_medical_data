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

def save_data(house_data, session, data):
	try:
		logger.debug('start to save data %s', house_data)
		parsed = json.loads(house_data)
		price = float(parsed.get('taxvaluedollarcnt'))
		parcle_id = parsed.get('parcelid')
		record = data.get(parcle_id)
		if record:
			log_error = float(record[1])
			timestamp = record[2]
		else:
			log_error = ''
			timestamp = ''			

		statement = "INSERT INTO %s (parcle_id, taxvaluedollarcnt, transaction_date, log_error) VALUES ('%s','%f','%s','%f')" %(table, parcle_id, price,timestamp,log_error)
		logger.info('begin into cassandra %s', statement)
		session.execute(statement)
		logger.info('saved data into cassandra %s', statement)

	except Exception as e:
		logger.error('cannot save data %s', house_data)

def shutdown_hook(consumer, session):
	logger.info('closing resource')
	consumer.close()
	session.shutdown()
	logger.info('released resource')

if __name__ == '__main__':
	#setup command line argument

	parser = argparse.ArgumentParser()
	parser.add_argument('topic_name', help='the kafka topic name to subscribe from')
	parser.add_argument('kafka_broker', help= 'the kafka broker address')
	parser.add_argument('cassandra_broker', help= 'the cassandra borker location')
	parser.add_argument('keyspace', help= 'the keyspace')
	parser.add_argument('table', help= 'the table in cassandra')
	parser.add_argument('file1', help= 'file1 to join')
	parser.add_argument('file2', help= 'file2 to join')

	# -parse argument
	args = parser.parse_args()
	topic_name = args.topic_name
	kafka_broker = args.kafka_broker
	cassandra_broker = args.cassandra_broker
	keyspace = args.keyspace
	table = args.table
	file1 = args.file1
	file2 = args.file2

	# create kafka consumer
	consumer = KafkaConsumer(
		topic_name,
		bootstrap_servers = kafka_broker
	)

	# create a cansandra session
	cassandra_cluster = Cluster(
		contact_points = cassandra_broker.split(',')
	)
	session = cassandra_cluster.connect()

	session.execute("CREATE KEYSPACE IF NOT EXISTS %s WITH replication = {'class':'SimpleStrategy', 'replication_factor':'3'}" % keyspace)
	session.set_keyspace(keyspace)
	session.execute("CREATE TABLE IF NOT EXISTS %s (parcle_id text,taxvaluedollarcnt float, transaction_date text, log_error float, PRIMARY KEY (parcle_id))" % table)

	fo1 = open(file1, "r")
	fo2 = open(file2, "r")

	line = fo1.readline().strip()
	attributes = line.split(',')
	
	data = {}

	newlines = fo1.readlines()

	for newline in newlines:
		features = newline.strip().split(',')
		data[features[0]] = features
    
	newlines = fo2.readlines()

	for newline in newlines:
		features = newline.strip().split(',')
		data[features[0]] = features        

	atexit.register(shutdown_hook, consumer, session)

	for msg in consumer:
		# logger.debug(msg)
		save_data(msg.value, session, data)

