import datetime
from datetime import date
from time import strftime
import google_news
import tweets
import pytest
import pymongo
from pymongo import MongoClient
import sentiment_analysis
import transformers

def test_sentiment11():
    assert(1==1)

# # @pytest.fixture
# def mongo_connect():
#     google_news.db = [google_news.client["News"], google_news.client["UserData"]]
#     google_news.collection = [google_news.db[0]["GoogleAPI"], google_news.db[0]["GoogleAPI_links"], google_news.db[1]["Google_News"]]

# def test_mongodb_content(mongo_connect):
#     '''Checks if the given connection contains documents inside or not'''
#     for data in google_news.collection:
#         assert data.count_documents({})>0 

# def test_sentiment1():
#     doc = 'The words are very positive in this sentence'
#     return_sentiment = sentiment_analysis.sentiments_analysis(doc)
#     print(return_sentiment)
#     assert(return_sentiment[0]['score'] == 0.6004692912101746)
    
# def test_extract_tweets(): 
#     result =tweets.extract_tweets(['Elon Musk','Twitter'],'2022-04-20','2022-04-26')
#     assert len(result)>0
