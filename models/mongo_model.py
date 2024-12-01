from pymongo import MongoClient

# MongoDB Database Connection
client = MongoClient("mongodb://localhost:27017/")
db = client.hybrid_db

def fetch_mongo_data(query):
    # Example: Parse MongoDB query
    result = db.example_collection.find_one({"name": query})
    return result
