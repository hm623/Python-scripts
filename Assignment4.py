output:

CSUN@Hassans-MacBook-Air comp467 % python3 comp467db.py

Databases: ['mydatabase', 'sample_mflix', 'admin', 'local']

The database exists.

Collections: ['customers']

The collection exists.

Inserted document ID: 67bd1272a5527cb54de7072e

 

code (followed W3 step by step instructions):

 

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
