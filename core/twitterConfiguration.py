import tweepy

def getKeys ():
    return {
        'CONSUMER_KEY': 'v8WVqaVjd7Kt9eFGnyb92qdsA',
        'CONSUMER_SECRET': 'uublp5tFbQDX2ggZrB08FZPEr1AptKQIMd4pZMrAxzAISm7Zrh',
        'ACCESS_TOKEN': '798223587001962500-94uioR5IIXfhuxTC8w5vZ7HZeiAFpwo',
        'ACCESS_SECRET': 'WCWZenjd6EmwT5eTuvH3inqSkHnv4lfjt73NPLHaA8yOe'
    }

def getAuth ():
    configKeys = getKeys()
    auth = tweepy.OAuthHandler(configKeys['CONSUMER_KEY'], configKeys['CONSUMER_SECRET'])
    auth.set_access_token(configKeys['ACCESS_TOKEN'], configKeys['ACCESS_SECRET'])

    return auth

def getApi ():
    auth = getAuth()

    return tweepy.API(auth)