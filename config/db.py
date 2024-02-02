from pymongo import MongoClient
MONGO_URI= "mongodb+srv://anjalamongodb:mongodb@cluster0.b3vxizb.mongodb.net/Notes"
try:
    connection =MongoClient(MONGO_URI)
except Exception as e:
    print(e)