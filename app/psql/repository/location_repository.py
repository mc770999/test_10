from sqlalchemy.exc import SQLAlchemyError

from app.psql.database import session_maker
from app.psql.models import Location


def create_location(new_location):
    try:
        with session_maker() as session:
            session.add(new_location)
            session.commit()  # Commit the transaction to the database

        return new_location  # Return the created Location object
    except SQLAlchemyError as e:
        session.rollback()  # Rollback in case of error
        print(f"Error creating location: {str(e)}")
        return str(e)

# 2. Read Operation (R)
def get_location_by_id(location_id):
    try:
        with session_maker() as session:
            location = session.query(Location).filter_by(id=location_id).first()
            return location  # Return the Location object or None if not found
    except SQLAlchemyError as e:
        print(f"Error retrieving location: {str(e)}")
        return None

def get_all_locations():
    try:
        with session_maker() as session:
        # Retrieve all locations
            locations = session.query(Location).all()
            return locations  # Return a list of Location objects
    except SQLAlchemyError as e:
        print(f"Error retrieving locations: {str(e)}")
        return []

# 3. Delete Operation (D)
def delete_location_by_id(location_id):
    try:
        with session_maker() as session:
            # Retrieve the location to be deleted
            location = session.query(Location).filter_by(id=location_id).first()
            if location:
                session.delete(location)  # Delete the location
                session.commit()  # Commit the transaction to the database
                return True  # Return True if deletion was successful
            else:
                return False  # Location not found
    except SQLAlchemyError as e:
        session.rollback()  # Rollback in case of error
        print(f"Error deleting location: {str(e)}")
        return False