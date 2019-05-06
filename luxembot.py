'''
A simple twitterbot that tweets random Wikipedia articles relating to Luxembourg

https://twitter.com/luxembot
'''

import tweepy
import json
import random
import time


CRED_PATH = 'credentials.json'
LINKS_PATH = 'links.txt'

TWEET_INTERVAL = 1 # Time between tweets in minutes


if __name__ == '__main__':
    with open(CRED_PATH, 'r') as f:
        cred = json.load(f)

    # Create OAuth handler
    auth = tweepy.OAuthHandler(cred['consumer_key'], cred['consumer_secret'])
    auth.set_access_token(cred['access_token'], cred['access_token_secret'])

    api = tweepy.API(auth)

    with open(LINKS_PATH, 'r') as f:
        links = [line for line in f.readlines()]

    while True:
        link = random.choice(links)
        api.update_status('Here\'s another fact about Luxembourg:\n' + link)

        time.sleep(TWEET_INTERVAL * 60)