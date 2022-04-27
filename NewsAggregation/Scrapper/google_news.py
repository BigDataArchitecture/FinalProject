from gnewsclient import gnewsclient
import pymongo
import pandas as pd
import nltk
nltk.download('punkt')
from newspaper import Article
Topics = ['Business','World','Nation','Business','Technology','Entertainment','Sports','Science','Health']
Country = ['Australia','Canada ','India ', 'New Zealand', 'Nigeria', 'Pakistan', 'Africa', 
'United Kingdom', 'United States','France','Brazil','Russia', 'Ukraine','United Arab Emirates','China', 'Taiwan', 
           'Hong Kong', 'Japan', 'Republic of Korea']

client = pymongo.MongoClient("mongodb+srv://team3:qHovInc8WtqPBs7k@newsmonitor.uzcq9.mongodb.net/UserData?retryWrites=true&w=majority")
print(client["UserData"])
db = client["UserData"]
collection = db["Google_News"]

def remove(string):
    return string.replace(" ", "")

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
                print(article.summary,article.title)
                collection.insert_one({
                "news_title":article.title,
                "news_summary":article.summary,
                "news_text":article.text,
                "new_authors":article.authors,
                "news_top_image":article.top_image,
                "news_topic": i, #Putting news topic
                "news_Country": j, #puting news country
                "news_source": remove(a[k]['title'].split("-",1)[1]) #putting news source
                })
                print("Inserted",article.title)
            except:
                print("Cannot do NLP on this:",a[k]['link'] )


            
            
    