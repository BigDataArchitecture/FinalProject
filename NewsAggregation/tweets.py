import snscrape.modules.twitter as sntwitter
import json
from langdetect import detect
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import itertools
import snscrape.modules.twitter as sntwitter
import plotly.graph_objects as go
from datetime import datetime

def extract_tweets():
    input_keyword = input('Enter keywords for scraping separated by space')
    print("\n")
    keywords = input_keyword.split()
# print list
    print('list: ', keywords)
    input_start_time = input('Enter start date in yyyy-dd-mm')
    start=input_start_time
    input_end_time = input('Enter end date in yyyy-dd-mm')
    end=input_end_time

    for keyword in keywords:
        tweets = pd.DataFrame(itertools.islice(sntwitter.TwitterSearchScraper(f'"{keyword} lang:en since:{start} until:{end}"').get_items(),10 ))
        print(tweets)
    return tweets


if __name__ == "__main__":
  tweets=  extract_tweets()
  tweets