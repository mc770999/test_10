# Suspicious Explosive Content Model
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.psql.models import Base

class ExplosiveMessages(Base):
    __tablename__ = 'explosive_messages'

    id = Column(Integer, primary_key=True)
    content = Column(String, nullable=False)
    person_id = Column(Integer, ForeignKey('people.id'))

    person = relationship('Person', back_populates='explosive_message')

    def __repr__(self):
        return f"<SuspiciousExplosiveContent(id={self.id}, content={self.content})>"