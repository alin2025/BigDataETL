'''
https://rapidapi.com/mpeng/api/stock-and-options-trading-data-provider/
'''

import json
import requests
from kafka import KafkaProducer
topic3 = 'stook'
brokers = "course-kafka:9092"

url = "https://stock-and-options-trading-data-provider.p.rapidapi.com/options/aapl"

headers = {
	"X-RapidAPI-Proxy-Secret": "a755b180-f5a9-11e9-9f69-7bf51e845926",
	"X-RapidAPI-Key": "5f7df78670msh470977d57fc0e58p1bfd80jsnaa924711be5b",
	"X-RapidAPI-Host": "stock-and-options-trading-data-provider.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)
row = response.json()
print(response.text)

producer = KafkaProducer(
	bootstrap_servers=brokers,
	client_id='producer',
	acks=1,
	compression_type=None,
	retries=3,
	reconnect_backoff_ms=50,
	reconnect_backoff_max_ms=1000,
	value_serializer=lambda v: json.dumps(row).encode('utf-8'))

producer = KafkaProducer(bootstrap_servers=brokers)
producer.send(topic=topic3, value=json.dumps(row).encode('utf-8'))
producer.flush()