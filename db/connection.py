from pymongo import MongoClient
from config import MONGO_URI
def connect():
    client = MongoClient(MONGO_URI)
    if client:
        return client
