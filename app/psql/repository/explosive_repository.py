from sqlalchemy.exc import SQLAlchemyError
from typing import List

from app.psql.database import session_maker
from app.psql.models import ExplosiveMessages


def create_message(new_messages_explode : List[ExplosiveMessages]):
    try:
        with session_maker() as session:

            session.add_all(new_messages_explode)
            session.commit()
            for message in new_messages_explode:
                session.refresh(message)

        return [m.id for m in new_messages_explode]
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error creating message_explode: {str(e)}")
        return str(e)


def get_message_explode_by_person_id(person_id):
    try:
        with session_maker() as session:
            message_explode = session.query(ExplosiveMessages).filter_by(person_id=person_id).all()
            return message_explode
    except SQLAlchemyError as e:
        print(f"Error retrieving message_explode: {str(e)}")
        return []


def get_all_message_explodes():
    try:
        with session_maker() as session:
            # Retrieve all message_explodes
            message_explodes = session.query(ExplosiveMessages).all()
            return message_explodes  # Return a list of ExplosiveMessages objects
    except SQLAlchemyError as e:
        print(f"Error retrieving message_explodes: {str(e)}")
        return []


# 3. Delete Operation (D)
def delete_message_explode_by_person_id(person_id):
    try:
        with session_maker() as session:
            # Retrieve the message_explode to be deleted
            message_explode = session.query(ExplosiveMessages).filter_by(person_id=person_id).all()
            if message_explode:
                session.delete(message_explode)  # Delete the message_explode
                session.commit()  # Commit the transaction to the database
                return True  # Return True if deletion was successful
            else:
                return False  # ExplosiveMessages not found
    except SQLAlchemyError as e:
        session.rollback()  # Rollback in case of error
        print(f"Error deleting message_explode: {str(e)}")
        return False