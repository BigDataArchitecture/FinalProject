###This is twitter Scrapping Code

##This code helps us in getting tweets which are related to the news keywords


import snscrape.modules.twitter as sntwitter
import json
import numpy as np
import pandas as pd
import itertools
from datetime import datetime

def extract_tweets(keywords,input_start_time,input_end_time):
  count = len(keywords)
  print(count)
  for i in range(len(keywords)):
    temp = keywords[:count:]
    count = count - 1
    print(temp)
    tweets = pd.DataFrame(itertools.islice(sntwitter.TwitterSearchScraper(f'"{temp} lang:en since:{input_start_time} until:{input_end_time}"').get_items(),10 ))
    if len(tweets) > 0:
      return tweets
    else:
      continue
