from sqlalchemy.exc import SQLAlchemyError

from app.psql.database import session_maker
from app.psql.models import Person, Device, Location, ExplosiveMessages, HostageMessages


def create_person_on_psql(person):
    try:
        with session_maker() as session:
            session.add(person)
            session.commit()
            session.refresh(person)

        return person.id

    except SQLAlchemyError as e:
        session.rollback()
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

def get_person_by_email(t_email):
    try:
        with session_maker() as session:

            person = (session.query(Person).filter_by(email=t_email)
            .join(Device,Device.person_id == Person.id)
            .join(Location,Location.person_id == Person.id)
            .outerjoin(ExplosiveMessages,ExplosiveMessages.person_id == Person.id)
            .outerjoin(HostageMessages,HostageMessages.person_id == Person.id)
            .first()
            )
            print(person.to_dict())
            return person.to_dict()

    except SQLAlchemyError as e:
        print(f"Error retrieving person: {str(e)}")
        return None


