# Person Model
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
import datetime
from app.psql.models import Base
from sqlalchemy.orm import relationship


class Person(Base):
    __tablename__ = 'people'

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    username = Column(String, nullable=False)
    ip_address = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=True)


    location = relationship('Location', back_populates='people', cascade='all, delete-orphan')
    device = relationship('Device', back_populates='people', cascade='all, delete-orphan')
    explosive_message = relationship('ExplosiveMessages', back_populates='person', cascade='all, delete-orphan')
    hostage_messages = relationship('HostageMessages', back_populates='person')

    def __repr__(self):
        return f"<Person(email={self.email}, username={self.username}, created_at={self.created_at})>"

    def to_dict(self):
        return {
            "id" : self.id,
            "email" : self.email,
            "username" : self.username,
            "ip_address" : self.ip_address,
            "created_at" : self.created_at,
            "location" : next(l.to_dict() for l in self.location),
            "device":next(d.to_dict() for d in self.device),
            "explosive_message":[m.to_dict() for m in self.explosive_message] ,
            "hostage_messages": [m.to_dict() for m in self.hostage_messages]
        }