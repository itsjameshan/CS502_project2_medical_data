Zillow House Price Prediction
================

Introduction
------------

This is a data pipeline project that predicts the sale price of House sold on Zillow, visualizes the trend, and using machine learning compared with the Zestimate prediction. Ideally, we will implement the Microservicee architecture using Spark, Hadoop, MapReduce, Mesos, Cassandra and Kafka (SMACK) stack and the front-end tool Superset.

Data Source
-----------

-   [Zillow data from Kaggle](https://www.kaggle.com/c/zillow-prize-1#description)

Architecture
------------

![](images/architecture.png)

Evaluation
--------------

###

-   Mean Absolute Error
SparkML are evaluated on Mean Absolute Error between the predicted log error and the actual log error. The log error is defined as

'logerror=log(Zestimate)−log(SalePrice)'

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

Reference
---------

[xxxxxx](http://xxxxxxx)
