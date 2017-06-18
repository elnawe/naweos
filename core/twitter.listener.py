import tweepy
import twitterConfiguration
from datetime import datetime

auth = twitterConfiguration.getAuth()
api = twitterConfiguration.getApi()

class TwitterListener (tweepy.StreamListener):

    def on_data (self, data):
        try:
            with open('responses/mentions.json', 'a') as f:
                f.write(data)

                api.update_status('@nawetimebomb Message received at ' + datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S'))
                
                return True
        except BaseException as e:
            print 'Error: %s' %(e)

        
        return True

    def on_error (self, error):
        print error

        return True

twitterListener = TwitterListener()
twitterStream = tweepy.Stream(auth=auth, listener=twitterListener)
twitterStream.filter(follow='1223565589', track=['@naweos'])