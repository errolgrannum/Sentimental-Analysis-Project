from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

#import project keys + other project configuration data
from config import *


class listener (StreamListener):

	def on_data(self, data):
		print data
		return True

	def on_error(self, status):
		print status

# we need to authorize ourselves
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth,listener())
twitterStream.filter(track=["Howard,University"])
