from datetime import datetime

from app.psql.models import Person, Location, HostageMessages, ExplosiveMessages, Device


def convert_to_person(person_json):
    # Convert the main `Person` attributes
    person = Person(
        email=person_json.get("email", "no@email"),
        username=person_json.get("username", "no_user_name"),
        ip_address=person_json.get("ip_address", "no_ip_address"),
        created_at=datetime.fromisoformat(person_json["created_at"]) if person_json.get("created_at") else None
    )

    return person

def convert_to_location(person_id, person_json):
    location_data = person_json.get("location", {})
    location = Location(
        latitude=location_data.get("latitude", "no_latitude"),
        longitude=location_data.get("longitude", "no_longitude"),
        city=location_data.get("city", "no_city"),
        country=location_data.get("country", "no_country"),
        person_id = person_id
    )
    return location

def convert_to_hostages(person_id, person_json):
    hostages_messages = [
        HostageMessages(
            content=message,
            person_id=person_id
        ) for message in person_json.get("sentences",[])
    ]
    return hostages_messages

def convert_to_expensive(person_id, person_json):
    hostages_messages = [
        ExplosiveMessages(
            content=message,
            person_id=person_id
        ) for message in person_json.get("sentences",[])
    ]
    return hostages_messages


def convert_to_device(person_id, person_json):
    json_device = person_json.get("device", {})
    device = Device(
        browser=json_device.get("browser", "no_browser"),
        os=json_device.get("os", "no_os"),
        device_id=json_device.get("device_id", "no_device_id"),
        person_id=person_id
    )
    return device