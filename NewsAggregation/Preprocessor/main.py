from gnewsclient import gnewsclient
import pymongo
import pandas as pd
import nltk
from sentiment_analysis import sentiments_analysis
from keyword_generation import keyword_gen
from tweets import extract_tweets
import uvicorn
from fastapi import FastAPI, File,HTTPException

nltk.download('punkt')
from newspaper import Article

app = FastAPI()

@app.get('/preprocessor/')
def google_news(url,tweets = False):
    def remove(string):
        return string.replace(" ", "")
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()
    keywords = keyword_gen(article.summary)
    if tweets == True:
        tweets = extract_tweets(keywords)
        print(tweets)
        return tweets
    else:
        return {
            "news_link" : url,
            "news_title":article.title,
            "news_data":article.publish_date,
            "news_summary":article.summary,
            "news_text":article.text,
            "new_authors":article.authors,
            "news_top_image":article.top_image,
            "news_keywords":keywords,
            "news_sentiments":sentiments_analysis(article.summary)}
            
@app.get("/")
def welcome():
     return "Hi"

if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8002, reload=True)