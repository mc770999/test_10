from sqlalchemy.exc import SQLAlchemyError

from app.psql.database import session_maker
from app.psql.models import Device


def create_device(new_device : Device):
    try:
        with session_maker() as session:

            session.add(new_device)
            session.commit()
            session.refresh(new_device)

        return new_device.id  # Return the created Device object
    except SQLAlchemyError as e:
        session.rollback()  # Rollback in case of error
        print(f"Error creating device: {str(e)}")
        return str(e)


# 2. Read Operation (R)
def get_device_by_id(device_id):
    try:
        with session_maker() as session:
            device = session.query(Device).filter_by(id=device_id).first()
            return device  # Return the Device object or None if not found
    except SQLAlchemyError as e:
        print(f"Error retrieving device: {str(e)}")
        return None


def get_all_devices():
    try:
        with session_maker() as session:
            # Retrieve all devices
            devices = session.query(Device).all()
            return devices  # Return a list of Device objects
    except SQLAlchemyError as e:
        print(f"Error retrieving devices: {str(e)}")
        return []


# 3. Delete Operation (D)
def delete_device_by_id(device_id):
    try:
        with session_maker() as session:
            # Retrieve the device to be deleted
            device = session.query(Device).filter_by(id=device_id).first()
            if device:
                session.delete(device)  # Delete the device
                session.commit()  # Commit the transaction to the database
                return True  # Return True if deletion was successful
            else:
                return False  # Device not found
    except SQLAlchemyError as e:
        session.rollback()  # Rollback in case of error
        print(f"Error deleting device: {str(e)}")
        return False