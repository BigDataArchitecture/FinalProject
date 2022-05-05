import pymongo

client = pymongo.MongoClient("mongodb+srv://team3:qHovInc8WtqPBs7k@newsmonitor.uzcq9.mongodb.net/UserData?retryWrites=true&w=majority")
print(client["UserData"])
db = client["UserData"]
collection = db["Flask_mongo"]

# ##Insert into a collection
# collection.insert_one({"_id":5, "user_name":"Soumi"})
# print("Insert Done")

# ##Update a collection
# collection.find_one_and_update({"_id":"0"}, {"$set" : {"user_name" : "updated_user_name"}}, upsert = True )
# print("Update Done")

# ##Delete a collection
# collection.delete_one({"_id":0, "user_name":"Soumi"})
# print("Delete Done")

##read data
a = collection.find()
for data in a:
    print(data)

##read specific column
# Fields with values as 1 will
# only appear in the result
x = collection.find({},{'_id': 0, 'user_name': 1})
for data in x:
    print(data)

##find with query
myquery = { "user_name": "updated_user_name" }
mydoc = collection.find(myquery)
for data in mydoc:
    print(data)


# import certifi
# print(certifi.where())