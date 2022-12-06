# Twitter Search
  
This is a Streamlit app that allows you to search for tweets containing a specified search term from a given Twitter handle. It also displays some stats about the user's profile.

## Prerequisites  

To use this app, you will need to have the following installed:  

- Python 3.7 or later
- Tweepy
- Streamlit

  
## Usage  

To run the app, open a terminal and navigate to the directory where the app is located. Then, run the following command:

```streamlit run twitterSearchStreamLit.py```  

A new window will open in your default browser, and you can use the app by entering a Twitter handle and a search term. The app will then display the found tweets and the user's stats.

## Customization    


You can customize the app by modifying the following variables in the twitterSearchStreamLit.py file:

- consumer_key: Your Twitter API consumer key
- consumer_secret: Your Twitter API consumer secret
- access_key: Your Twitter API access key
- access_secret: Your Twitter API access secret
- default_since: The default "since" date for the date input fields
- default_until: The default "until" date for the date input fields
- num_tweets: The maximum number of tweets to retrieve from the user's timeline