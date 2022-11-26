import pymongo

client = pymongo.MongoClient("mongodb+srv://believerfit1:garg1234@cluster0.oukmjdc.mongodb.net/?retryWrites=true&w=majority")
db = client.test


d = {
    "name":"abc",
    "job":"xyz",
    "salary": "xxxxxx"
}


db1=client['mongotest']
coll = db1['test']
coll.insert_one(d)