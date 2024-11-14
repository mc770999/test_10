from sqlalchemy.exc import SQLAlchemyError
from typing import List

from app.psql.database import session_maker
from app.psql.models import HostageMessages


def create_message(new_messages_explode : List[HostageMessages]):
    try:
        with session_maker() as session:

            session.add_all(new_messages_explode)
            session.commit()
            for message in new_messages_explode:
                session.refresh(message)

        return [m.id for m in new_messages_explode]
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error creating message_hostage: {str(e)}")
        return str(e)


def get_message_hostage_by_person_id(person_id):
    try:
        with session_maker() as session:
            message_hostage = session.query(HostageMessages).filter_by(person_id=person_id).all()
            return message_hostage
    except SQLAlchemyError as e:
        print(f"Error retrieving message_hostage: {str(e)}")
        return []


def get_all_message_hostages():
    try:
        with session_maker() as session:
            message_hostages = session.query(HostageMessages).all()
            return message_hostages
    except SQLAlchemyError as e:
        print(f"Error retrieving message_hostages: {str(e)}")
        return []



def delete_message_hostage_by_person_id(person_id):
    try:
        with session_maker() as session:

            message_hostage = session.query(HostageMessages).filter_by(person_id=person_id).all()
            if message_hostage:
                session.delete(message_hostage)
                session.commit()
                return True
            else:
                return False
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error deleting message_hostage: {str(e)}")
        return False