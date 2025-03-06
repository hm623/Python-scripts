import pymongo

client = pymongo.MongoClient("mongodb+srv://myusername:mypassword@mycluster.cpy3e.mongodb.net/")

db = client["mydatabase"]

dblist = client.list_database_names()
print("Databases:", dblist)

if "mydatabase" in dblist:
print("The database exists.")

mycol = db["customers"]

collist = db.list_collection_names()
print("Collections:", collist)

if "customers" in collist:
print("The collection exists.")


mydict = {"name": "John", "address": "Highway 37"}
x = mycol.insert_one(mydict)


print("Inserted document ID:", x.inserted_id)
