# importing all the libraries 

import tweepy 
import pandas as pd 
import sys # to take arguments from the terinla 
from login_function import login
import json 

# declaring  the credentials  

consumer_key = '4LZh8tlui4hy0FiBc0El7Mh19' 
consumer_secret = 'ImOmm5sm2wUBaBoTVSFDPAEH1LPlmqaPIkua8d3PNscYZw0mFA'

access_token = '1114502658507730945-607tyGyU0eHitRxasTR64lczyX3kff'
access_secret = 'sDEMuCVT3l93FuTfCCI0YEqnmYSDAr2hnm2vWip3lZqkc'

# handling the authentication process of the twitter api 

api = login(consumer_key, consumer_secret, access_token, access_secret)

DATA_DIR = str(sys.argv[1]) # add the location for the source file  
OUT_DIR_JSON = str(sys.argv[2]) # add the location for the output file in JSON file 

# get the user_ids as a python list 

def get_id(filepath):
	df = pd.read_json(filepath, lines=True)
	return df.id.to_list()

user_ids = get_id(filepath)


# retrieving the user tweets and storing them in a jsonstream file 
# dyanmically doing it, and using file handling for it 

for i in user_ids:
	try:
		data = {}
		timeline = tweepy.Cursor(api.user_timeline, user_id=i, ).items()
		data[i] = []
		for status in timeline:
			obj = status._json
			tweet = {}
			tweet['tweet_id'] = obj['id']
			tweet['created_at'] = obj['created_at']
			tweet['text'] = obj['text']
			tweet['retweeted'] = obj['retweeted']
			tweet['retweet_count'] = obj['retweet_count']
			tweet['hashtags'] = len(obj['entities']['hashtags'] )
			tweet['user_mentions'] = len(obj['entities']['user_mentions'])
			data[i].append(tweet)
		j = json.dumps(data)
		f = open("dict.jsonstream", 'a')
		f.write(j)
		f.close()
		print("no. of tweets of the user",len(data[i]))
		print('\n')
	except tweepy.error.TweepError:
		print('error')
