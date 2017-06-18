import tweepy
import twitterConfiguration

api = twitterConfiguration.getApi()
mentions = open('responses/mentions.json').readlines()
lastMentionIndex = len(mentions) - 1

api.update_status