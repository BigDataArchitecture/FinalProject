import google_news
import tweets
import pytest

@pytest.fixture
def topics_list():
    '''Returns a Wallet instance with a zero balance'''
    return len(google_news.Topics)>0

@pytest.fixture
def country_list():
    '''Returns a Wallet instance with a zero balance'''
    return len(google_news.Country)>0

# @pytest.fixture
# def ():
#     '''Returns a Wallet instance with a zero balance'''
#     tweets.input_end_time
#     return len(google_news.Country)>0

def test_topics_nonempty(topics_list):
    '''Checks whether the given topics list is not empty or not'''
    assert len(google_news.Topics)>0

def test_country_nonempty(country_list):
    '''Checks whether the given topics list is not empty or not'''
    assert len(google_news.Country)>0