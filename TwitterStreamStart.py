from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time


#import project keys + other project configuration data
from config import *


def sentimentAnalysis(text):
	pass


class listener (StreamListener):

	def on_data(self, data):
		tweet = data.split(',"text":"')[1].split('","source')[0]
		sentimentRating = sentimentAnalysis(tweet)

		save = tweet + '::' + sentimentRating +'\n'
		output = open('output.csv', 'a')
		output.write(save)
		output.close()
		# print data
		return True

	def on_error(self, status):
		print status

# we need to authorize ourselves
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth,listener())
twitterStream.filter(track=["Howard,University"])
