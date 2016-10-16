#!/usr/bin/env python
import tweepy
import os
from config import(consumer_key, consumer_secret,access_token,\
                     access_token_secret )


class TwitterAPI(object):
    '''
    Authenticate requests to Twitter API using Tweepy and fetch tweets.
    '''


    def __init__(self):
        '''
        Setup Twitter API Authentication.
        Get your keys from ``https://apps.twitter.com/app/new``
        '''
        self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        self.auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(self.auth)

    def fetch_tweets(self, max_id = -1):
        '''
        Fetches tweets with #custserv and RT count >=1 in a chronological order.
        Input: ``max_id`` optional parameter.
                Extract 100 tweets from this ``max_id``

        Returns ``result``: list of dictionary of all relevant tweets.
        '''
        result = []
        querystring = '#custserv'  # Query parameter, to search in tweets.
        max_tweets = 100           # 100 is the max Twitter API permits in one
                                   # request.
        max_id = int(max_id)       # max_id is obtained from `app.py`

        try:
            if max_id <= 0:
                # If ``max_id`` isn't provided, default value = -1
                new_tweets = self.api.search(q=querystring, count=max_tweets)
            else:
                new_tweets = self.api.search(q=querystring, count=max_tweets,
                                        max_id=str(max_id - 1))
            # In case no new tweets are found.
            if not new_tweets:
                pass
            # Iterate through all tweets and extract relevant ones.
            for tweet in new_tweets:
                if tweet.retweet_count > 0:
                    if tweet not in result:
                        # Prevents duplicate tweet ids to be added.
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
