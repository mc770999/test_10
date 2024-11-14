# Location Model
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.psql.models import Base

class Location(Base):
    __tablename__ = 'locations'

    id = Column(Integer, primary_key=True)
    latitude = Column(String, nullable=False)
    longitude = Column(String, nullable=False)
    city = Column(String, nullable=False)
    country = Column(String, nullable=False)
    person_id = Column(Integer, ForeignKey('people.id'))

    people = relationship("Person", back_populates='location')

    def __repr__(self):
        return f"<Location(city={self.city}, country={self.country}, latitude={self.latitude}, longitude={self.longitude})>"
