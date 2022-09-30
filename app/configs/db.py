from pymongo import MongoClient
from pymongo.collection import Collection
from app.loader import MONGO_CLUSTER, MONGO_COLLECTION


cluster = MongoClient()
db = cluster[MONGO_CLUSTER]
collection: Collection = db[MONGO_COLLECTION]
