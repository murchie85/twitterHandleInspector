import tweepy

import sys
sys.path.append('../')
from k import *

# TOKENS IMPORTED AT PARENT REPO


# authenticate with the Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# prompt the user for an account name and search term
account = input("Enter a Twitter account name: ")
search_term = input("Enter a search term: ")

# search for tweets from the given account that match the search term
tweets = tweepy.Cursor(api.search, q=search_term, lang="en", tweet_mode="extended",
                       since_id='2020-01-01', screen_name=account).items(10)

# print the tweets
for tweet in tweets:
    print(tweet.full_text)
    print('')