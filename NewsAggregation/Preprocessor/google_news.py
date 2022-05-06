from gnewsclient import gnewsclient
import pymongo
import pandas as pd
import nltk
from sentiment_analysis import sentiments_analysis
from keyword_generation import keyword_gen
from tweets import extract_tweets


nltk.download('punkt')
from newspaper import Article

Topics = ['Business','World','Nation','Business','Technology','Entertainment','Sports','Science','Health']
Country = ['Australia','Canada ','India ', 'New Zealand', 'Nigeria', 'Pakistan', 'Africa', 
'United Kingdom', 'United States','France','Brazil','Russia', 'Ukraine','United Arab Emirates','China', 'Taiwan', 
           'Hong Kong', 'Japan', 'Republic of Korea']

client = pymongo.MongoClient("mongodb+srv://team3:qHovInc8WtqPBs7k@newsmonitor.uzcq9.mongodb.net/UserData?retryWrites=true&w=majority")
print(client["News"])
db = client["News"]
collection = db["GoogleAPI_links_2"]

def remove(string):
    return string.replace(" ", "")

insert = 0
not_insert = 0
# ##Insert into a collection
for i in Topics:
    for j in Country:
        client = gnewsclient.NewsClient(language='English', location=j, topic=i)
        a = client.get_news()
        for k in range(len(a)):
            try:
                article = Article(a[k]['link'])
                article.download()
                article.parse()
                article.nlp()
                keywords = keyword_gen(article.summary)
                tweets = extract_tweets(keywords)
                collection.insert_one({
                "news_link" : a[k]['link'],
                "news_title":article.title,
                "news_data":article.publish_date,
                "news_summary":article.summary,
                "news_text":article.text,
                "new_authors":article.authors,
                "news_top_image":article.top_image,
                "news_topic": i, #Putting news topic
                "news_Country": j, #puting news country
                "news_source": remove(a[k]['title'].split("-",1)[1]), #putting news source
                "news_keywords":keywords,
                "news_sentiments":sentiments_analysis(article.summary),
                "news_tweets": tweets})
                insert = insert + 1
                print("Inserted",insert)
                # print("Inserted",article.publish_date)
            except:
                not_insert = not_insert + 1
                print("Cannot do NLP",not_insert)
print("Inserted:",insert, "Not Inserted:",not_insert)


            
            
    