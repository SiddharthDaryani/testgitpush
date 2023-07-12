import pymongo
import urllib.parse
username = urllib.parse.quote_plus("siddharthdaryani")
password = urllib.parse.quote_plus("sidd@SQL567")
client= pymongo.MongoClient(f"mongodb+srv://{username}:{password}@siddharth.ipwvs0o.mongodb.net/?retryWrites=true&w=majority")
db= client.test
print(db)
d= {
    "name":"Siddharth",
    "surname":"Daryani",
    "email":"siddharth@gmail.com"
}
db1= client['mongotest']
coll= db1['test']
coll.insert_one(d)