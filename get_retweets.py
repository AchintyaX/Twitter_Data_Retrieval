# importing all the libraries 

import tweepy 
import pandas as pd 
import sys # to take arguments from the terinla 
from login_function import login
import json 

# declaring the credentials 
consumer_key = '' 
consumer_secret = ''

access_token = ''
access_secret = ''

# handling the authentication process of the twitter api 

api = login(consumer_key, consumer_secret, access_token, access_secret)

DATA_DIR = str(sys.argv[1]) # add the location for the source file  
OUT_DIR_JSON = str(sys.argv[2]) # add the location for the output file in JSON file 

# get the user_ids as a python list 

def get_id(filepath):
	df = pd.read_json(filepath, lines=True)
	return df.tweet_id.to_list()

user_ids = get_id(DATA_DIR)

tweet_ids = ['847393742424203264', '847401296332177409', '847402865010266113','847403775165779968', '847404320463044608']
for i in tweet_ids:
    try :
        data = {}
        # the object created here is a status object hence you can get all the properties
        retweets = api.retweets(i, count=100)
        data[i] = []
        for retweet in retweets:
            info = {}
            retweet = retweet._json
            info['tweet_id'] = retweet['id']
            info['user_id'] = retweet['user']['id_str']
            data[i].append(info)
        j = json.dumps(data)
        f = open.('retweet_dict.jsonstream', 'a')
        f.write(j)
        f.close()
        print("no. of retweets of the user", len(data[i]))
        print('\n')
    except tweepy.error.TweepError:
        print('error')



    
