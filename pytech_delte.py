from pymongo import MongoClient

url="mongodb+srv://admin:admin@cluster0.3chly.mongodb.net/test";

conn = MongoClient(url)

db = conn.pytech

collection = db.students

cursor = collection.find()

for record in cursor:

print(record)
