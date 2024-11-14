import json
import os

from dotenv import load_dotenv
from flask import Flask
from kafka import KafkaProducer, KafkaConsumer

from app.mongo_db.repository.users_repository import insert_person
from app.psql.models import Person

load_dotenv(verbose=True)

def consume_messages():
    consumer = KafkaConsumer(
        os.environ["TOPIC_ALL_MESSAGE_CONSUMER"],  # Changed to 'processed_messagess' topic
        bootstrap_servers=os.environ['BOOTSTRAP_SERVERS'],
        value_deserializer=lambda v: json.loads(v.decode('utf-8')),
        auto_offset_reset='earliest'
    )
    for message in consumer:
        ids = insert_person(message.value) #insrert to mongo
        print(f'Received({ids}): {message.key}:{message.value}')
    # ids = insert_person(consumer)
    # print(ids)

app = Flask(__name__)

if __name__ == '__main__':
    consume_messages()  # Changed function name to reflect messages context
    app.run()