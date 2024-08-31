'''
In this example we will monitor a log file and write its content the messages to a different target file. The pipeline is as follows:
1. An external generator (implemented by the log_generator notebook) will write logs to a log file.
2. A Kafka producer will monitor the log file and send to Kafka every new data.
3. A kafka consumer will consume the messages and write them to a destination file.
'''
from kafka import KafkaConsumer

# In this example we will illustrate a simple producer-consumer integration

topic2 = 'kafka-tst-02'
brokers = ["course-kafka:9092"]
target_file = '/home/developer/kafka/sinkFiles/tarFile.log'

# First we set the consumer, and we use the KafkaConsumer class to create a generator of the messages.
consumer = KafkaConsumer(
    topic2,
    group_id='File2File',
    bootstrap_servers=brokers,
    auto_commit_interval_ms=1000)

# Write the data to target file
with open(target_file, 'w') as f:
    for message in consumer:
        print(message.value)
        f.write(format(message.value))
        f.flush()
