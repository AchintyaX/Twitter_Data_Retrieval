# Import the necessary Libraries 

import pandas as pd 
import tweepy 
import sys
from login_function import login
# Set up the twitter API




api = login(consumer_key, consumer_secret, access_token, access_secret)
# import the file which contains the tweetData 
INPUT_DIR = str(sys.argv[1])

# File where the user data is to be dumped 
OUTPUT_DIR = str(sys.argv[2])

# defining the dictionary for the user data 

user_dict = {
	"user_name":[],
	"user_id":[],
	"screen_name":[],
	"location":[],
	"verified":[],
	"status_count":[],
	"num_followers":[],
	"list_followers_user_id":[],
	"list_followers_user_name":[], 
	"num_friends":[],
	"list_friends_user_id":[],
	"list_friends_user_name":[]
}

# getting the data 
df = pd.read_json(INPUT_DIR)
user_ids = df['user_id']

# getting the user information 

for i in user_ids:
	u = api.get_user(id=i)

	user_dict["user_name"].append(u.name)
	user_dict["user_id"].append(u.id)
	user_dict["screen_name"].append(u.screen_name)
	user_dict["location"].append(u.location)
	user_dict["verified"].append(u.verified)
	user_dict["status_count"].append(u.statuses_count)
	user_dict["num_followers"].append(u.followeres_count)
	followers_id = " "
	followers_name = " "
	for user in tweepy.Cursor(api.followers, user_id=i).items():
		followers_id = followers_id + user.id + " ," #getting the user_id of all the followers
		followers_name = followers_name + user.name + " ,"
	user_dict["list_followers_user_id"].append(followers_id)
	user_dict["list_followers_user_name"].append(followers_name)
	user_dict['num_friends'].append(u.friends_count)
	friends_id = " "
	friends_name = " "
	for user in tweepy.Cursor(api.friends, user_id=i).items():
		friends_id = friends_id + user.id + " ,"
		friends_name = friends_name + user.name + " ,"
	user_dict["list_friends_user_id"].append(friends_id)
	user_dict["list_friends_user_name"].append(friends_name)

# Converting the dictionary to dataframe 
user_data = pd.DataFrame(user_dict)

# Storing the dataframe in a json file 

user_data.to_json(path_or_buf=OUTPUT_DIR, orient='table')
