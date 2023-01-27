from kafka import KafkaProducer
from tweepy import OAuthHandler,Stream
import os

# Kafka settings
topic = os.getenv('KAFKA_TOPIC_NAME')
# setting up Kafka producer
producer = KafkaProducer(bootstrap_servers=os.getenv('KAFKA_SERVER') + ':' + os.getenv('KAFKA_PORT'))


#This is a basic listener that just put received tweets to kafka cluster.
class TweetsListener(Stream):
    def on_data(self, data):
        try:
            producer.send(topic = topic, value = data)
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True
 
# extract the topic from the env variable
WORDS_TO_TRACK = os.getenv('WORDS_TO_TRACK')

if __name__ == '__main__':
    #This handles Twitter authetification and the connection to Twitter Streaming API
    consumer_key, consumer_secret, access_token, access_token_secret = os.getenv('CONSUMER_KEY'), os.getenv('CONSUMER_SECRET') , os.getenv('ACCESS_TOKEN'), os.getenv('ACCESS_TOKEN_SECRET')
    stream = TweetsListener(consumer_key, consumer_secret, access_token, access_token_secret)
    # Goal is to keep this process always going
    while True:
        try:
            stream.filter(languages=["en"], track=WORDS_TO_TRACK)
        except:
            pass