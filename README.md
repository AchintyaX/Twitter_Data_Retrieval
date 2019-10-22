# COMMAND LINE TOOL FOR TWEETS FROM TWEET ID 

` python3 tweet_retrieve.py input_file output_file `
input_file - file containing the labels and the tweet IDs 
output_file - file containing the final data about the tweets retrieved 

# DEPENDENCIES 
1. Tweepy
2. Pandas 
3. sys 
# TWITTER API KEYS 
To use the script one needs to generate the keys to the twitter API, after a filling a set of questions you would get a consumer key and an Access Token 
link to the developer page is [here](https://developer.twitter.com/en/apply)

# MOTIVATION 

Data from twitter is widely used in NLP tasks, as it a social network website. A lot of Social Media analysis and prediction, human behavior analysis is being done using twitter data.

Recently twitter changed its data redistribution policy according to which people can't share the complete data they used for their research if it was obtained from twitter. 
What they can share are <b>`tweet IDs`</b>. 

Finding a way to retrieve all the tweet data from twitter is a tough task and writing a script for it is a very repetitive task. 
As a researcher I faced problem and a spent a significant amount of time finding the correct way to retrieve all the necessary data for my research project

I don't want budding researchers like me to face this problem again, and hence I am sharing the script that I wrote for this purpose 

# HELP 

If anyone wants further help in understanding the script
please contact me at - <b>achintyashankhdhar@gmail.com</b>

to know what all fields of data you can extract from twitter kindly check this [link](https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference/get-statuses-show-id)

## I HOPE I HELPED :)
