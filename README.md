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


Data Ingestion
--------------

### Kafka

-   User can specify currency and fetch bitcoin price by running xxxxx.
-   Zillow predicted log error will be sent to any kafka topic specified by user after SparkML processing.
-   Code can be found here: [xxxxxxx](fetch-bitcoin-price.py). Screenshot: ![](images/xxxxx.png) ![](images/xxxxx.png)

![](images/xxxxxx.png)

Data Storage
------------

### Cassandra

-   schema

| column\_name |    type   |
|:------------:|:---------:|
|   timestamp  | timestamp |
|   house xxxxx   |    text   |
|  log error |   float   |


-   PRIMARY KEY (parcelID, timestamp)

Data Computation
----------------

### Spark

Cluster Scheduling Layer
------------------------

### Mesos

​	
​
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
				a: Top 10 highest rating movie by a given month
				b: Top 10 rated movie by a given month
				c: Top rated month by a movie		
		Week 4: Starts and finishes unit testing
		
		Wei Cheng: Set UP Kafka, Data ingestion using kafka
		Week 1: Starts implement data transformation layer, Set up Kafka Connect to load data from Zillow csv to Cassandra   [xx% completed] (work with James)
		Week 2: Add error/exception handling and more comments in the source code
		Week 3: 
		Week 4: 
		
		Howie:  Data visualization
		Week 1: Set up UI, Determine the requirements to implement, get ready to fulfill the Nodejs module features;
		Week 2: Setup backend for data visualization; simple front end to display data
		Week 3: 
		Week 4: 


​	


Reference
---------

[xxxxxx](http://xxxxxxx)
