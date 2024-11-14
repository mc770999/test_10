from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.psql.models import Base


class Device(Base):
    __tablename__ = 'devices'

    id = Column(Integer, primary_key=True)
    browser = Column(String, nullable=False)
    os = Column(String, nullable=False)
    device_id = Column(String, nullable=False)
    person_id = Column(Integer, ForeignKey('people.id'))


    people = relationship('Person', back_populates='device')

    def __repr__(self):
        return f"<Device(device_id={self.device_id}, browser={self.browser}, os={self.os})>"

    def to_dict(self):
        return {
            "id":self.id,
            "browser":self.browser,
            "os":self.os,
            "device_id":self.device_id,
            "person_id":self.person_id
        }