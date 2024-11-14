import json
import os

from dotenv import load_dotenv
from flask import Flask
from kafka import KafkaProducer, KafkaConsumer

load_dotenv(verbose=True)

def consume_explosive():
    consumer = KafkaConsumer(
        os.environ["TOPIC_EXPLOSIVE_MESSAGE_CONSUMER"],
        bootstrap_servers=os.environ['BOOTSTRAP_SERVERS'],
        value_deserializer=lambda v: json.loads(v.decode('utf-8')),
        auto_offset_reset='earliest'
    )
    for message in consumer:

        print(f'Received: {message.key}:{message.value}')

app = Flask(__name__)

if __name__ == '__main__':
    consume_explosive()
    app.run()