'''Helps in getting tweets from twitter using snstwitter with the keywords provided
A module with "extract_tweets" main funtion extracts the tweets from twitter with specified filters.
First itteration will be done on all the keywords provided in the list, if nothing got from that we will keep on decresing the list
First element gets the highest weightage

Author: Parth Shah shah.parth3@northeastern.edu

Created at 27th April 2022

'''
import snscrape.modules.twitter as sntwitter
import json
import numpy as np
import pandas as pd
import itertools
from datetime import date
from datetime import timedelta

def twitter_dataframe_dict(df):
    """
    Performs converting a dataframe to dictionary for mongodb database
    Parameters:
    df : pandas.dataframe
        The dataframe for which we need the dictionary
    """
    tweet_df = {}
    count  = 0
    cols_list = df.columns.to_list()
    for index, row in df.iterrows():
        tweet_df[index] = {}
        for j in cols_list:
            tweet_df[index][j] = row[j]
        print(tweet_df)
        count = count + 1
    return tweet_df


def extract_tweets(keywords,input_start_time = date.today() - timedelta(days=7),input_end_time = date.today()):
    """
    Performs tweet extraction
    Parameters
    -------------------------
    keywords : list
        The list of keywords for which we need the tweets
    input_start_time : date ('YYYY-MM-DD')
        Start date from when tweets needed
    input_end_time : date ('YYYY-MM-DD')
        End date till tweets needed
    """
    print(input_end_time,input_start_time)
    count = len(keywords)
    for i in range(len(keywords)):
        temp = keywords[:count:]
        count = count - 1
        print(temp)
        tweets = pd.DataFrame(itertools.islice(sntwitter.TwitterSearchScraper(f'"{temp} lang:en since:{input_start_time} until:{input_end_time}"').get_items(),10 ))
        if len(tweets) > 0:
            return twitter_dataframe_dict(tweets)
        else:
            continue

#run when file is directly executed

if __name__ == '__main__':
    keywords = ['Elon Musk','Twitter']
    input_start_time = '2022-04-20'
    input_end_time = '2022-04-26'
    return_df = extract_tweets(keywords,input_start_time,input_end_time)
    assert(len(return_df) > 0) 
    
    
    
    