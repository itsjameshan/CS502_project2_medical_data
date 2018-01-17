# CS502_project2_medical_data
This is a data pipeline to analyze medical data

								New Drug Notification System : Find the drug that suit you 

## Introduction for business plan and pitch
	We are planning to create a new drug notification system for patients/physicians to use. The idea is
	simple, we are using the key words from patients/physicians to help us to look for the FDA (food and
	drug administration) data set for the drugs that is related to this type of disease. For example,
	patient with diabetes, we can look into the FDA’s data set to find drug that treat diabetes. We will
	build a data pipeline to store and parse the data from FDA website via Kafka and Cassandra. We will
	also apply machine learning model on the drugs that we receive from the data set and suggest the most
	suitable drug back to the patients. Depends on which attribute that the patient cares the most. Some
	patient may want a lower price drug, and some may not care about the price, but only on the
	effectiveness of the drug.

