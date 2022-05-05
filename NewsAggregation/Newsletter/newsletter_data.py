'''
Data fetching for our news letter
This module consist of data fetching of our newsletter for automated email 

Author Parth Shah shah.parth3@northeastern.edu'
Created at 4th May 2022
'''

import pymongo
import pandas as pd


def create_data(country,topic):
    '''
    This Function loads the data from our newsletter_data module and makes the template for our newsletter
    This is a customized function which takes in country and topic as input and select the data likewise
    Parameters:
    ---------------------
    country: string
        Name of the country for which news should be fetched
        Default: India🇮🇳
    topic: string
        Topic of the news for which news should be fetched
        Default: Business
    '''

    client = pymongo.MongoClient("mongodb+srv://team3:qHovInc8WtqPBs7k@newsmonitor.uzcq9.mongodb.net/UserData?retryWrites=true&w=majority")
    print(client["News"])
    db = client["News"]
    collection = db["GoogleAPI_links"]

    myquery = {"news_Country": country ,"news_topic": topic }
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

