# write data to any kafka cluster
# write data to any kafka topic
# scheduled fetch price from csv file

# parse command line argument
import argparse
import schedule
import time
import logging
import json
import boto3
import botocore
import pathlib
# atexit can be used to register shutdown_hook
import atexit

from kafka import KafkaProducer

#from alpha_vantage.timeseries import TimeSeries


logging.basicConfig()
logger = logging.getLogger('data-producer')

#debug, info, warn, error, fatal
logger.setLevel(logging.DEBUG)

filedir = ''
topic_name = ''
kafka_broker = ''
attributes = ''

def shutdown_hook(producer, fo):
    logger.info('closing kafka producer')
    producer.flush(10)
    producer.close(10)
    fo.close()
    logger.info('kafka producer closed!!')


def fetch_price_and_sent(producer, fo):
    logger.debug('about to fetch house info:')

    newline = fo.readline()

    if(newline == ''):
        exit()

    features = newline.split(',')


    data = {}

    for i in range(len(attributes)):
        data[attributes[i]] = features[i]

    data = json.dumps(data)
    #logger.info('retrieved one record: %s', data)

    try:
        producer.send(topic = topic_name, value = data)
        logger.debug('sent data to kafka %s', data)
    except Exception as e:
        logger.warn('failed to send house info to kafka')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filedir', help = ' the symbol of the stock')
    parser.add_argument('topic_name', help = 'the name of the topic')
    parser.add_argument('kafka_broker', help = 'the location of the kafka')

    args = parser.parse_args()
    filedir = args.filedir
    topic_name = args.topic_name
    kafka_broker = args.kafka_broker
    BUCKET_NAME = 'jameshantest' # replace with your bucket name

    producer = KafkaProducer(
        # if we have kafka cluster with 1000 nodes, what do we pass to kafka broker
        bootstrap_servers = kafka_broker
        )

    path = pathlib.Path(filedir)

    #if raw is not in local, then fetch from S3
    if path.is_file() == False:
        s3 = boto3.resource('s3')
        logger.warn('begin to load data from S3:%s', filedir)
        try:
            s3.Bucket(BUCKET_NAME).download_file('capstone/'+filedir, filedir)
            logger.warn('successfully load data from S3:%s', filedir)
        except botocore.exceptions.ClientError as e:
            if e.response['Error']['Code'] == "404":
                print("The object does not exist.")
            else:
                raise

    fo = open(filedir, "r")

    line = fo.readline()
    attributes = line.split(',')

    # Get json object with the intraday data and another with  the call's metadata

    fetch_price_and_sent(producer, fo)

    schedule.every(1).seconds.do(fetch_price_and_sent, producer, fo)
    atexit.register(shutdown_hook,producer, fo)

    while True:
        schedule.run_pending()
        time.sleep(1)