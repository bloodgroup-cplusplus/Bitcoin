"""Elasticsearch is a document-based NOSQL database meaning developers do not need any prior knowledge of SQL to use
	console.log('count', count);
Developers do not need any prior knowledge of SQL to use it.
It is a modern search and anlytics engine based on Apache License,
Focuses on search capabilities
Distributed in nature
Handle big data without hasshle
Used in Kibana Logstash
In this article, we will learn how to run Elasticsearch on a docker container and perform basic CRUD operations and different types of search operations using the python programming language."""



#connect python to elasticsearch go to terminal and type
# " pip ( or pip3 or pipx whatever works for you) install elasticsearch"



# lets try to connect to the ElasticSearch instance running in docker


from elasticsearch import Elasticsearch
es = Elasticsearch(["http://localhost:49154"]) # connecting to elasticsearch
print(es.ping())


""" Index in elasticsearch. As the name suggests , many might assume that this is the same as the indexing concept in other databases like MYSQL, MongDB etc. The simple answer is NO. Index in ElasticSearch represents a database where you store all the data. 

To insert a document we can directly use the "index()" function that accepts the index anme and the document data as paramets. 
Looping over each document in the list and calling the index functino to insert huge amounts of data will be time-consumeing. 
ES has the "bulk()" function for writing huge amount of data for now we stick with the function "index()"""


employees_data = [
    {
    'name': 'Vishnu',
    'age': 21,
    'programming_languages': ['C++', 'python', 'nodejs']
    },
    {
    'name': 'Sanjay',
    'age': 23,
    'programming_languages': ['python', 'C#']
    },
    {
    'name': 'Arjun',
    'age': 33,
    'programming_languages': ['C++', 'Ruby']
    },
    {
    'name': 'Ram',
    'age': 27,
    'programming_languages': ['Rust', 'python']
    }
]
for data in employees_data:
    es.index(index='employees', document=data)





