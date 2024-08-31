from kafka import KafkaProducer
import time,json,requests
from datetime import datetime

bootstrapServers = "course-kafka:9092"
topic1 = 'From_API_To_Kafka_job'

while True:
    # ======== Read from Remote API  ==================== #
    response = requests.get(url="https://data.cityofnewyork.us/resource/ic3t-wcy2.json")
    for line in range(len(response.json())):
        row = response.json()[line]
        print(row)
        time.sleep(2)
        #==============send to consumer==========================#
        producer = KafkaProducer(bootstrap_servers=bootstrapServers)
        producer.send(topic=topic1, value=json.dumps(row).encode('utf-8'))


# Json.dumps()=>> json.dumps() function converts a Python object into a json string
#https://www.geeksforgeeks.org/json-dumps-in-python/

# response.json() returns a JSON object of the result (if the result was written in JSON format, if not it raises an error
#https://www.geeksforgeeks.org/response-json-python-requests/


#api
# https://dev.socrata.com/foundry/data.cityofnewyork.us/ic3t-wcy2