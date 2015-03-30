#!/usr/bin/python
#Copyright Silicon Incorporated, 2015, All Rights Reserved

import tweepy, time

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)
me = api.me()

while True:
    try:
        for follower in tweepy.Cursor(api.followers, me).items():
            api.create_friendship(id=follower.id)
        for follower in tweepy.Cursor(api.friends, me).items():
            for friend in tweepy.Cursor(api.friends, follower.id).items():
                if friend.name != me.name: api.create_friendship(id=friend.id)
    except tweepy.TweepError, e:
        print "TweepError raised, ignoring and continuing."
        print e
        continue
