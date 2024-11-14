import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


from app.psql.models import Base

load_dotenv()

engine = create_engine(os.environ["DB_URL"])
session_maker = sessionmaker(bind=engine)

def init_db():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


init_db()
