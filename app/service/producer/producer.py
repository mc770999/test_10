import json
import os

from flask import Flask
from kafka import KafkaProducer
from dotenv import load_dotenv

from app.utils.explosive_or_hostage import contain_explosive, contain_hostage

app = Flask(__name__)

load_dotenv(verbose=True)


def produce_message(person: dict):
    kafka_producer = KafkaProducer(
        bootstrap_servers=os.environ['BOOTSTRAP_SERVERS'],
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    kafka_producer.send(
        os.environ["TOPIC_ALL_MESSAGE_CONSUMER"],
        value=person,
        key=person['id'].encode('utf-8')
    )

    if contain_explosive(person):
        kafka_producer.send(
            os.environ["TOPIC_EXPLOSIVE_MESSAGE_CONSUMER"] ,
            value=person,
            key=person['id'].encode('utf-8')
        )

    if contain_hostage(person):
        kafka_producer.send(
            os.environ["TOPIC_HOSTAGE_MESSAGE_CONSUMER"],
            value=person,
            key=person['id'].encode('utf-8')
        )

    kafka_producer.flush()

