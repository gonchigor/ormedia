import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]

mycol = mydb["customers"]

print(myclient.list_database_names())
print(mydb.list_collection_names())

mydict = {"name": "John", "address": "Highway 37"}

x = mycol.insert_one(mydict)
print(x.inserted_id)

print(myclient.list_database_names())
print(mydb.list_collection_names())
