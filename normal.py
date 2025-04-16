from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

uri = "mongodb+srv://dishaUser:mongodbArtysoul27@mycluster0.jpdmf.mongodb.net/"

try:
    client = MongoClient(uri, serverSelectionTimeoutMS=5000)
    client.server_info()  # Force connection
    print("MongoDB connection successful!")
except ConnectionFailure as e:
    print("MongoDB connection failed:", e)