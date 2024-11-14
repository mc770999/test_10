from app.mongo_db.connect import collection_people


def insert_person(user):
    result = collection_people.insert_one(user)
    # Return the inserted document's ID
    return result.inserted_id