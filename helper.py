from pymongo import MongoClient, errors, collection
import os

uri = os.environ.get("MONGO_URI", "mongodb://127.0.0.1:27017")
client = MongoClient(uri)
dbs = client["learn_english"]
db_vocab = dbs["vocabulary"]
