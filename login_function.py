import tweepy 

def login(consumer_key, consumer_secret, access_token, access_secret):
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_secret)

	api = tweepy.API(auth, wait_on_rate_limit_notify=True, wait_on_rate_limit=True)

	return api 