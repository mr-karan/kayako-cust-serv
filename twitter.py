#!/usr/bin/env python
import tweepy
import sys
import jsonpickle
import os


consumer_key = 'hYowzLI0JAgay0RNdygkWR6lt'
consumer_secret = 'cPWbxLbFbm4iiGHyHCPpI217OlKdW7syS50ixeL2fT8YGqahXz'
access_token ='71795977-cOueHTRpue2lttRlKaa6KRCDneRjjVu3PfPBvcnhv'
access_token_secret = '82ara22eJi8cwtD578jfFwq9Ka2Pg0qFJIXcUcnBIfem5'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

tweetCount = 0


def get_tweets(max_id = -1, sinceId = None):
    result = []
    searchQuery = '#custserv'  # this is what we're searching for
    tweetsPerQry = 100  # this is the max the API permits

    max_id = int(max_id)
    print("Twitter Max ID"+ str(max_id))
    print(type(max_id))
    sinceId = sinceId
    try:
        if (max_id <= 0):
            if (not sinceId):
                print("1")
                new_tweets = api.search(q=searchQuery, count=tweetsPerQry)
            else:
                print("2")
                new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                                        since_id=sinceId)
        else:
            if (not sinceId):
                print("3")
                new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                                        max_id=str(max_id - 1))
            else:
                print("4")
                new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                                        max_id=str(max_id - 1),
                                        since_id=sinceId)
        if not new_tweets:
            print("No more tweets found")

        for tweet in new_tweets:
            if tweet.retweet_count > 0:
                print(tweet.id)
                if tweet not in result:
                    result.append(
                    {'id':tweet.id,
                    'text':tweet.text,
                    'image':tweet.user.profile_image_url_https,
                    'name':tweet.user.screen_name,
                    'time':tweet.created_at}
                    )


        print(len(result))
        #print("Downloaded {0} tweets".format(tweetCount))
    except tweepy.TweepError as e:
        # Just exit if any error
        print("some error : " + str(e))
    return result
