from sqlalchemy.orm import declarative_base


Base = declarative_base()

from .location_model import Location
from .device_model import Device
from .person_model import Person
from .hostage_messages_model import HostageMessages
from .explosive_messages_model import ExplosiveMessages

