from sqlalchemy.exc import SQLAlchemyError

from app.psql.database import session_maker
from app.psql.models import Person


def create_person(email, username, ip_address, created_at):
    try:
        with session_maker() as session:
            new_person = Person(email=email, username=username, ip_address=ip_address, created_at=created_at)

            # Add the new Person object to the session
            session.add(new_person)
            session.commit()  # Commit the transaction to the database

        return new_person  # Return the created Person object
    except SQLAlchemyError as e:
        session.rollback()  # Rollback in case of error
        print(f"Error creating person: {str(e)}")
        return None

# 2. Read Operation (R)
def get_person_by_id(person_id):
    try:
        with session_maker() as session:
            person = session.query(Person).filter_by(id=person_id).first()
            return person  # Return the Person object or None if not found
    except SQLAlchemyError as e:
        print(f"Error retrieving person: {str(e)}")
        return None

def get_all_persons():
    try:
        with session_maker() as session:
        # Retrieve all persons
            persons = session.query(Person).all()
            return persons  # Return a list of Person objects
    except SQLAlchemyError as e:
        print(f"Error retrieving persons: {str(e)}")
        return []

# 3. Delete Operation (D)
def delete_person_by_id(person_id):
    try:
        with session_maker() as session:
            # Retrieve the person to be deleted
            person = session.query(Person).filter_by(id=person_id).first()
            if person:
                session.delete(person)  # Delete the person
                session.commit()  # Commit the transaction to the database
                return True  # Return True if deletion was successful
            else:
                return False  # Person not found
    except SQLAlchemyError as e:
        session.rollback()  # Rollback in case of error
        print(f"Error deleting person: {str(e)}")
        return False