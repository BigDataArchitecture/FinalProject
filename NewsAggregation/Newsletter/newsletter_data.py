import pymongo
import pandas as pd


def create_data():
    client = pymongo.MongoClient("mongodb+srv://team3:qHovInc8WtqPBs7k@newsmonitor.uzcq9.mongodb.net/UserData?retryWrites=true&w=majority")
    print(client["News"])
    db = client["News"]
    collection = db["GoogleAPI_links"]

    myquery = {"news_Country": "Australia"}
    mydoc = collection.find(myquery)

    data_dict = {}

    data_columns = ["news_title","news_summary","news_top_image","news_source","news_sentiments","news_link"]

    actual_data = {}
    news_counter = 0
    for i in mydoc:
        if news_counter == 7:
            break
        else:
            actual_data[str(news_counter)] = i
            news_counter = news_counter + 1

    news_counter = 1
    for k in range(6):
        data_dict[str(k)] = {}
        for i in range(len(data_columns)):
            data_dict[str(k)][data_columns[i]+str(news_counter)] = actual_data[str(k)][data_columns[i]]
        news_counter  = news_counter + 1   

    return data_dict 

