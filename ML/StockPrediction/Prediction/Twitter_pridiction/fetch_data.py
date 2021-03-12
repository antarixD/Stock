#!/usr/bin/env python
# encoding: utf-8

import tweepy
import csv
from datetime import timedelta
import datetime
import pandas as pd
import tabulate

#Twitter API credentials
consumer_key = "4cP3SXcVQYbsm6XgU4m1SufRe"
consumer_secret = "rgeZajux9kb20LJ5l03EDqErrf9R4GXjFOFV4X6J8HGEiOaIuL"
access_key = "1296554839019646976-DktsUlS9TRuI7L7lpithjGU5tdtq5s"
access_secret = "GMtArRyG8jyTuHef9TB75TxHNZDVyM0Pxa0XpPQJ0dI6j"





def get_all_tweets(screen_name):
    #Twitter only allows access to a users most recent 3240 tweets with this method

    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    #initialize a list to hold all the tweepy Tweets
    alltweets = []

    #make initial request for most recent tweets (200 is the maximum allowed count)
    #AX
    #new_tweets = api.user_timeline(screen_name = screen_name,count=2)
    new_tweets  = api.search(screen_name, count=1000, lang='en', exclude='retweets',
                    tweet_mode='extended')

    #save most recent tweets
    alltweets.extend(new_tweets)

    #save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1

    #keep grabbing tweets until there are no tweets left to grab
    length_of_tweets = 0


    #while length_of_tweets < 200 :
    while len(new_tweets) > 0:
        print ("getting tweets before %s" % (oldest))

        #all subsiquent requests use the max_id param to prevent duplicates
        #AX
        #new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
        new_tweets = api.search(screen_name, count=1000, lang='en', exclude='retweets',
                    tweet_mode='extended')

        #save most recent tweets
        alltweets.extend(new_tweets)


        #update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1
        length_of_tweets = (len(alltweets))



        print ("...%s tweets downloaded so far" % (len(alltweets)))



        outtweets = [[tweet.id_str, tweet.created_at, tweet.full_text.encode("utf-8"), tweet.user.screen_name] for tweet in alltweets]

        df_tweets = todf(outtweets)
    return(outtweets)

def todf(outtweets):
    column_names = ["tweet_id", "created_at", "text", "user"]
    tweet_df = pd.DataFrame(outtweets, columns=column_names)
    tweet_df.to_csv('tcs.csv')
    return tweet_df





if __name__ == '__main__':
    #pass in the username of the account you want to download
    tweets = get_all_tweets("TCS")
    df_tweets = todf(tweets)
  #  print(df_tweets)
 #   df_tweets.to_csv('tcs.csv')
