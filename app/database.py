from pymongo import MongoClient
from datetime import datetime
import uuid

def store_in_mongodb(trends, ip_address):
    client = MongoClient("mongodb://localhost:27017/")
    db = client['twitter_trends']
    collection = db['trending_topics']

    unique_id = str(uuid.uuid4())
    record = {
        "_id": unique_id,
        "trend1": trends[0],
        "trend2": trends[1],
        "trend3": trends[2],
        "trend4": trends[3],
        "trend5": trends[4],
        "timestamp": datetime.now(),
        "ip_address": ip_address
    }

    collection.insert_one(record)
    return record
