from kafka import KafkaConsumer
from elasticsearch import Elasticsearch
import json

#pip install elasticsearch
# Kafka configuration
kafka_topic = 'my_trip'
kafka_bootstrap_servers = ['course-kafka:9092']

# Elasticsearch configuration
es = Elasticsearch([{'host': 'elasticksearch', 'port': 9200, 'scheme': 'http'}])
es_index = 'nyctaxi'

# Create a Kafka consumer
consumer = KafkaConsumer(
    kafka_topic,
    bootstrap_servers=kafka_bootstrap_servers,
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

# Consume messages from Kafka and write them to Elasticsearch
for message in consumer:
    document = message.value
    es.index(index=es_index, body=document)

print("Finished consuming messages and indexing to Elasticsearch.")