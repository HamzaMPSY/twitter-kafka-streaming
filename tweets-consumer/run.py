import json
import os

from kafka import KafkaConsumer

# setting up Kafka consumer

if __name__ == '__main__':
    consumer = KafkaConsumer(
        os.getenv("KAFKA_TOPIC_NAME"),
        bootstrap_servers=os.getenv(
            'KAFKA_SERVER') + ':' + os.getenv('KAFKA_PORT'),
        value_deserializer=lambda x: json.loads(x.decode('utf-8')))

    for message in consumer:
        tweets = json.loads(json.dumps(message.value))
        print(message.value) 
