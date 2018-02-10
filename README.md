Zillow House Price Prediction
================

Introduction
------------

This is a data pipeline project that predicts the sale price of House sold on Zillow, visualizes the trend, and using machine learning compared with the Zestimate prediction. Ideally, we will implement the Microservicee architecture using Spark, Hadoop, MapReduce, Mesos, AKKA, Cassandra and Kafka (SMACK) stack and the front-end tool Superset.

Data Source
-----------

-   [Zillow data from Kaggle](https://www.kaggle.com/c/zillow-prize-1#description)


Architecture
------------
![](images/architecture.png)
-   [SMACK](http://bigdata-madesimple.com/smackspark-mesos-akka-kafka/)
-   [MicroService](https://www.linkedin.com/pulse/how-go-from-lamp-microservices-eric-macdougall/)

Evaluation
--------------

###

-   Mean Absolute Error
SparkML are evaluated on Mean Absolute Error between the predicted log error and the actual log error. The log error is defined as

`logerror=log(Zestimate)−log(SalePrice)`

and it is recorded in the transactions training data. If a transaction didn't happen for a property during that period of time, that row is ignored and not counted in the calculation of MAE.

Data source:
The original house history records files are stored in AWS S3:
https://s3.amazonaws.com/jameshantest/capstone/properties_2016.csv， 
https://s3.amazonaws.com/jameshantest/capstone/properties_2017.csv 

Data Ingestion
--------------
### Kafka

-   read properties_2016.csv and properties_2017.csv files from AWS S3, and then ingest each record to kafka cluster.
-   Zillow predicted log error will be sent to any kafka topic specified by user after SparkML processing.
-   Code can be found here: [xxxxxxx](fetch-bitcoin-price.py). Screenshot: ![](images/xxxxx.png) ![](images/xxxxx.png)

### important comands:
Start: zookeeper
./bin/zookeeper-server-start.sh config/zookeeper.properties &
Stop: zookeeper
./bin/zookeeper-server-stop.sh config/zookeeper.properties & 

Start: Kafka
./bin/kafka-server-start.sh -daemon config/server.properties &

![](images/xxxxxx.png)

Data Storage
------------

### Cassandra

-   schema

| column\_name |    type   |
|:------------:|:---------:|
|   parcle_id  |    text   |
|   log_error  |    float  |
|taxvaluedollarcnt|  text  |
|transaction_date|   text  |

-   PRIMARY KEY (parcelID, timestamp)
### important comands:
Run Cassandra:
bin/cassandra

Kill cassandra:
# user=`whoami`
# pgrep -u $user -f cassandra | xargs kill -9

see Cassandra status:
bin/nodetool status

run CQL:
./bin/cqlsh 172.31.82.134
use houseprice;  (Keyspace)
select * from house limit 20;

Data Computation
----------------

### Spark

Cluster Scheduling Layer
------------------------
Install spark:
wget https://archive.apache.org/dist/spark/spark-2.1.0/spark-2.1.0-bin-hadoop2.7.tgz
In master node:
./sbin/start-master.sh

In slave node:
./sbin/start-slave.sh spark://ip-172-31-89-32.ec2.internal:7077

WebUI:
http://54.163.44.28:8080/

Pyspark:
./bin/pyspark spark://ip-172-31-89-32.ec2.internal:7077
​
Submit python:
./bin/spark-submit --jars ~/code/spark-streaming-kafka-0-8-assembly_2.11-2.0.0.jar ~/code/data-stream.py

AWS set up 
---------------
Running data ingestion script:
python data_producer.py properties_2016.csv test1 172.31.89.32:9092
python data_producer.py properties_2017.csv test1 172.31.89.32:9092
​
Running data storage script:
python data_storage_aws.py test1 172.31.89.32:9092 54.163.44.28,34.207.87.67,54.164.0.73 houseprice house train_2016_v2.csv train_2017.csv

Deliverable
---------------

	Week1: Figure out project architecture, data source, determine the requirements and the functionalities to implement
	Week2: Each team member starts implementing their own module
	Week3: Each team member finishes their own module
	Week4: Testing, Report documenting		
	
	Detail Ownerships:
	
		James Han: 
		Week 1: Set up Spark on AWS, Cassandra on AWS
		Week 2: Implement SparkML to calucalte log error to indicaste the accuracy of silumation of house sale                               price.
		Week 3: Finishes implement data transformation layer: 
			(1) Aggregate the data into formats to support the Cassandra data schemas in (2)
			(2) Configure Cassandra data schema to support:
				a: The predicted log error comapred wtih train log error
				b: key matric indicate house sale pricing
				c: dynamic log eroor in a time series manner.		
		Week 4: Starts and finishes unit testing
		
		Wei Cheng: Set UP data infrastructure clusters on AWS with Kafka, zookeeper, Cassandra and Spark, implement Data ingestion code
		Week 1: Starts implement data transformation layer, Set up Kafka Connect to load data from Zillow csv to Cassandra   [xx% completed] (work with James)
		Week 2: Implement the data ingestion layer code using kafka in local machine environment
		Week 3: Deploy a zookeeper cluster, a kafka cluster and a spark cluster on AWS with 3 EC2 instances, and run data ingestion on AWS property
		Week 4: Deploy a 3-nodes' Cassandra Cluster, Test and verify the system function on AWS
		
		Howie:  Data visualization
		Week 1: Set up UI, Determine the requirements to implement, get ready to fulfill the Nodejs module features; For the UI we are planing to use Node.js or Apache Superset (https://superset.incubator.apache.org/) depending on which one has better integration with Amazon AWS. For me is probably Node.js since we have done it in class. The A
		Week 2: Setup backend for data visualization; simple front end to display data
		Week 3: Display the UI with the data input 
		Week 4: Testing and finish the function of the UI



​	


Reference
---------

[xxxxxx](http://xxxxxxx)
