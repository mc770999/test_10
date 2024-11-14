import os

import pymongo
from datetime import datetime
from bson import ObjectId
from dotenv import load_dotenv

load_dotenv(verbose=True)
# Connect to MongoDB
client = pymongo.MongoClient(os.environ["MONGO_DB"])
db = client["smart_listening_idf"]  # Database name
collection_people = db["people"]  # Collection name