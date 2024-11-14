import json
import os

from dotenv import load_dotenv
from flask import Flask
from kafka import KafkaProducer, KafkaConsumer

load_dotenv(verbose=True)

def consume_hostages():
    consumer = KafkaConsumer(
        os.environ["TOPIC_HOSTAGE_MESSAGE_CONSUMER"],  # Changed to 'processed_messagess' topic
        bootstrap_servers=os.environ['BOOTSTRAP_SERVERS'],
        value_deserializer=lambda v: json.loads(v.decode('utf-8')),
        auto_offset_reset='earliest'
    )
    for message in consumer:
        print(f'Received: {message.key}:{message.value}')

app = Flask(__name__)

if __name__ == '__main__':
    consume_hostages()  # Changed function name to reflect messages context
    app.run()