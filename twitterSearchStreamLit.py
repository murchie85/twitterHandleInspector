
import tweepy
import streamlit as st
from datetime import datetime
from datetime import date,timedelta
import sys
sys.path.append('../')
from k import *

# Authenticate with the Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

# Set up the Streamlit app
st.title("Twitter Search")
handle = st.text_input("Enter a Twitter handle:")
search_term = st.text_input("Enter a search term:")


# Set the default date range for the date input fields
default_since = date.today() - timedelta(days=7)
default_until = date.today()

# Get the selected date range from the user
since_date = st.date_input("Since:", value=default_since)
until_date = st.date_input("Until:", value=default_until)





# Check for invalid time ranges
if since_date < until_date and search_term and handle:

    # Get the user's profile
    user = api.get_user(handle)


    # Search for tweets
    tweets = tweepy.Cursor(api.user_timeline, screen_name=handle, since=since_date, until=until_date).items(1000)
    found_tweets = [tweet for tweet in tweets if search_term.lower() in tweet.text.lower()]
    print(found_tweets)


    # Display the found tweets
    st.subheader(f"Tweets containing '{search_term}' from @{handle}:")
    for tweet in found_tweets:
        st.write(tweet.text)



    # Display the user's stats
    st.subheader(f"Stats for @{handle}:")
    st.write(f"Number of tweets: {user.statuses_count}")
    st.write(f"Bio: {user.description}")
    st.write(f"Number of followers: {user.followers_count}")
    st.write(f"Number of friends: {user.friends_count}")

