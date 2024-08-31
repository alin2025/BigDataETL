from kafka import KafkaConsumer

# In this example we will illustrate a simple producer-consumer integration

bootstrapServers = "course-kafka:9092"
topic1 = 'From_API_To_Kafka'

# First we set the consumer,
consumer = KafkaConsumer(topic1,bootstrap_servers=bootstrapServers)

# print the value of the consumer
# we run the consumer to fetch the message scoming from topic1.
for message in consumer:
    print(str(message.value))