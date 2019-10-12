# importing tweepy used to connect twitter with python

import tweepy

# setting up the api keys for the twitter api 

consumer_key = '4LZh8tlui4hy0FiBc0El7Mh19' 
consumer_secret = 'ImOmm5sm2wUBaBoTVSFDPAEH1LPlmqaPIkua8d3PNscYZw0mFA'

access_token = '1114502658507730945-607tyGyU0eHitRxasTR64lczyX3kff'
access_secret = 'sDEMuCVT3l93FuTfCCI0YEqnmYSDAr2hnm2vWip3lZqkc'

# handling the authentication process of the twitter api
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

DATA_DIR = ' '  #  add the location for the source file 
OUT_DIR = ' ' # add location for the output file

import pandas as pd 

def retrieve_tweets(DATA_DIR, OUT_DIR):
	df = pd.read_csv(DATA_DIR, sep='\t') # check the file type if it is a csv then you don't need to define `sep`
	tweet_IDs = df.iloc[:, 0] # considering the tweet ids are the first column
	labels = df.iloc[:, 1] # considering the tweet ids are the 2nd column
	
	# fields we are retrieving 

	tweets_dict = {"tweet_id":[],
               "user_name":[],
               "user_id":[],
               "screen_name":[],
               "user_location":[],
               "follower_count":[],
               "friend_count":[],
               "text":[],
               "retweet_count":[],
               "created_at":[],
               "label":[]
              }

    for i in range(len(tweet_IDs)):
    	# retrieving the tweets using the twitter api
    	# we need to take care of the tweets that have been deleted, so we are doing some error handling 
    	try:
        	tweet = api.get_status(tweet_IDs[i])
    
        	tweets_dict['tweet_id'].append(tweet_IDs[i])
        	tweets_dict['user_name'].append(tweet.user.name)
        	tweets_dict['user_id'].append(tweet.user.id)
        	tweets_dict['screen_name'].append(tweet.user.screen_name)
        	tweets_dict['user_location'].append(tweet.user.location)
        	tweets_dict['follower_count'].append(tweet.user.followers_count)
        	tweets_dict['friend_count'].append(tweet.user.friends_count)
        	tweets_dict['text'].append(tweet.text)
        	tweets_dict['retweet_count'].append(tweet.retweet_count)
        	tweets_dict['created_at'].append(tweet.created_at)
        	tweets_dict['label'].append(labels[i])
    	except tweepy.error.TweepError:
        	print('error')
	print(len(tweets_dict['label']))

	tweet_data = pd.DataFrame(tweets_dict)

	tweet_data.to_csv(OUT_DIR, index=False)


retrieve_tweets(DATA_DIR, OUT_DIR)
    