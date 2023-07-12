import pymongo
client= pymongo.MongoClient("mongodb+srv://ineuron:mongodb123@siddharth.ipwvs0o.mongodb.net/?retryWrites=true&w=majority")
db= client.test
print(db)
