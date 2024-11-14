import json
import os

from dotenv import load_dotenv
from flask import Flask
from kafka import KafkaProducer, KafkaConsumer

from app.psql.repository.device_repository import create_device
from app.psql.repository.location_repository import create_location
from app.psql.repository.person_repository import create_person_on_psql
from app.utils.convert_to_models import convert_to_person, convert_to_device, convert_to_location

load_dotenv(verbose=True)

def consume_explosive():
    consumer = KafkaConsumer(
        os.environ["TOPIC_EXPLOSIVE_MESSAGE_CONSUMER"],
        bootstrap_servers=os.environ['BOOTSTRAP_SERVERS'],
        value_deserializer=lambda v: json.loads(v.decode('utf-8')),
        auto_offset_reset='earliest'
    )
    for message in consumer:
        person = convert_to_person(message.velue)
        person_id = create_person_on_psql(person)
        device_id = create_device(convert_to_device(person_id,person))
        location_id = create_location(convert_to_location(person_id,person))

        print(f'Received: person_id : {person_id}, device_id : {device_id}, location_id : {location_id}')

app = Flask(__name__)

if __name__ == '__main__':
    consume_explosive()
    app.run()