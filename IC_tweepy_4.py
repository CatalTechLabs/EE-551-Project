# Ilker Catal, icatal@stevens.edu
# EE/CPE 551 Class Project (run in Python 2.x)
# I have fallowed tutorials from below sources:
											# https://pypi.org
											# http://docs.tweepy.org/en/latest/

import keys	 
import tweepy as tw
import csv

class TweeterListener(tw.StreamListener): # defining tweeter Stream listener class 

	def on_data(self,data): # this function is called when new data arrives to listenner
		print(data)
		return True
	
	def process_data(self,data):
		with open('saved_tweet.txt','a') as tf:
			tf.write(data)
		return True	

# this function listens for error status code 420.
# returning false on first function disconnects the stream
	def on_error(self, status): 
		print(status)
		if status == 420:
			return False	

if __name__ == "__main__": #Calling main function

	listener =TweeterListener()
	
	# authenticating keys that were given from tweeter which resides as module in
	# a seperate file keys.py. Imported here on top
	auth = tw.OAuthHandler(keys.consumer_key,keys.consumer_secret)
	auth.set_access_token(keys.access_token,keys.access_token_secret)
	api = tw.API(auth)
	
	stream = tw.Stream(auth, listener)
	stream.filter(track=['Covid'])	# search twitter for "Covid"
	stream.filter(languages=['en','fr','es']) # filter for English, French and Spanish 

# Write data returned from twitter to "tweets.csv" using "csv" module
csvFile = open('tweets.csv')
csvWriter = csv.writer(csvfile)

csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
print tweet.created_at, tweet.text
csvFile.close()

