import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import os
import json

def process_or_store(tweet):
    print(json.dumps(tweet))

ckey = 'I532Q0QjcuGPKoagKARGs71a5'
consumer_secret = '8Fal9QovsYTg7M6nwZZNMeZRN6yQcu0T8EjCThYWFWX3TKCEpv'
access_token_key = '766041412097961985-d9JNgywCNFyIMGtgxNCMCyBMuc1UMxY'
access_token_secret = 'XJwKHr2PBK3omA6W7Y8cRWUMnMNryWW8hknpo3h9dRujg'



auth = OAuthHandler(ckey, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)

api = tweepy.API(auth)

for status in tweepy.Cursor(api.home_timeline).items(5):
    # Process a single status
    print(status.text)

class MyListener(StreamListener):

    def on_data(self, data):
        try:
            with open('python.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print('Error_on_data:',str(e))
            return True

        def on_error(self, status):
            print(status)
            return True


if __name__ == '__main__':
    listener = MyListener()
    auth = OAuthHandler(ckey, consumer_secret) #OAuth object
    auth.set_access_token(access_token_key, access_token_secret)
    twitter_stream = Stream(auth, listener)
    twitter_stream.filter(track=['#iPhone'])