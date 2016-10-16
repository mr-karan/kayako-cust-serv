#!/usr/bin/env python
import tweepy
import os
from config import(consumer_key, consumer_secret,access_token,\
                     access_token_secret )

# Setup Twitter API Authentication. Get your keys from ``https://apps.twitter.com/app/new``

class TwitterAPI(object):
    def __init__(self):
        self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        self.auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(self.auth)

    def fetch_tweets(self, max_id = -1):
        result = []
        querystring = '#custserv'  # Query parameter, to search in tweets.
        max_tweets = 100           # 100 is the max Twitter API permits in one request.
        max_id = int(max_id)       # max_id is obtained from `app.py`

        try:
            if max_id <= 0:
                new_tweets = self.api.search(q=querystring, count=max_tweets)
            else:
                new_tweets = self.api.search(q=querystring, count=max_tweets,
                                        max_id=str(max_id - 1))
            # In case no new tweets are found
            if not new_tweets:
                pass
            # `result`
            for tweet in new_tweets:
                if tweet.retweet_count > 0:
                    if tweet not in result:
                        result.append(
                        {'id':tweet.id,
                        'text':tweet.text,
                        'image':tweet.user.profile_image_url_https,
                        'name':tweet.user.screen_name,
                        'time':tweet.created_at}
                        )

        except tweepy.TweepError as e:
            print("Error : " + str(e))

        return result
