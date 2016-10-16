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

searchQuery = '#NobelPrize'  # this is what we're searching for
maxTweets = 10000000 # Some arbitrary large number
tweetsPerQry = 100  # this is the max the API permits
fName = 'tweets.txt' # We'll store the tweets in a text file.


# If results from a specific ID onwards are reqd, set since_id to that ID.
# else default to no lower limit, go as far back as API allows
sinceId = None

# If results only below a specific ID are, set max_id to that ID.
# else default to no upper limit, start from the most recent tweet matching the search query.
max_id = 787091551960780800

tweetCount = 0
print("Downloading max {0} tweets".format(maxTweets))
while tweetCount < maxTweets:
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
            break
        tweet = new_tweets[0]
        print((tweet.entities['urls']))
        tweetCount += len(new_tweets)
        print("Downloaded {0} tweets".format(tweetCount))
        max_id = new_tweets[-1].id
        print("MAX ID"+ str(max_id))
        print("Since ID"+ str(sinceId))
    except tweepy.TweepError as e:
        # Just exit if any error
        print("some error : " + str(e))
        break

print ("Downloaded {0} tweets, Saved to {1}".format(tweetCount, fName))
