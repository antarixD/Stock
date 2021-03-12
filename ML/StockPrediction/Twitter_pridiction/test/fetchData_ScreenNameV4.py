
import tweepy
import csv
from datetime import timedelta
import datetime
import pandas as pd
import tabulate
import ML.utils.datefile as dateUtils
import ML.utils.fileSystem as fileUtils
import ML.utils.pd_file as pdUtils
import os

#Twitter API credentials
consumer_key = "4cP3SXcVQYbsm6XgU4m1SufRe"
consumer_secret = "rgeZajux9kb20LJ5l03EDqErrf9R4GXjFOFV4X6J8HGEiOaIuL"
access_key = "1296554839019646976-DktsUlS9TRuI7L7lpithjGU5tdtq5s"
access_secret = "GMtArRyG8jyTuHef9TB75TxHNZDVyM0Pxa0XpPQJ0dI6j"

# ----------------Dates-------------------------#
today = dateUtils.currentDate()
last_day = dateUtils.yesterday(today)
last_day = last_day.strftime('%d-%m-%Y')
today = today.strftime('%d-%m-%Y')


start_date= dateUtils.getWorkingDate(5)
print(start_date)

#----------------create directory to save data----------------------#

parent_dir = "data/"
directory = 'tweets_' + today
fileUtils.createDir(parent_dir, directory)
column_names = ["user","tweet_id", "created_at", "text"]



def get_all_tweets(screen_name,column_names):
    auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)


    #initialize a list to hold all the tweepy Tweets
    alltweets = []

    new_tweets = api.user_timeline(screen_name,count=1000, lang='en', include = 'retweets',
                                   tweet_mode='extended')

    #save most recent tweets
    #adding the new_tweets to alltweets
    alltweets.extend(new_tweets)

    #save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1
    #---------Save time to filter out tweets with date -------------------#
    currentTime =alltweets[-1].created_at
    #-----------get the desired tweets from alltweets list-----------------------#
    outtweets = [[tweet.user.screen_name, tweet.id_str, tweet.created_at, tweet.full_text.encode("utf-8")] for tweet in
                 alltweets]
    #---------Save tweets independent as per date in Data directory-------------------#
    todf(outtweets,screen_name,today,column_names)

    #--------------filtering tweets as per time -----------------#
    while currentTime > start_date:

        print ("getting tweets before %s" % (oldest))

        #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name, count=1000, lang='en',include = 'retweets',
                    tweet_mode='extended',max_id=oldest)


        #save most recent tweets
        alltweets.extend(new_tweets)

        #update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1
        length_of_tweets = (len(alltweets))
        currentTime = new_tweets[-1].created_at

        print ("...%s tweets downloaded so far" % (len(alltweets)))

        outtweets = [[tweet.user.screen_name,tweet.id_str, tweet.created_at, tweet.full_text.encode("utf-8")] for tweet in alltweets]
        # ---------Save tweets independent as per date in Data directory-------------------#
        todf(outtweets,screen_name,today,column_names)
    #-----------concatinating/union all tweets--------------------#
    dataConcat(parent_dir,directory,last_day,column_names)
    return(outtweets)

def todf(outtweets,screen_name,today,column_names):
    #last_day = last_day.strftime('%d-%m-%Y')
    #column_names = ["user","tweet_id", "created_at", "text"]
    tweet_df = pd.DataFrame(outtweets, columns=column_names)
    tweet_df.to_csv('data/tweets_'+today+'/'+screen_name+'.csv')
    return tweet_df

def dataConcat(parent_dir,directory,last_day,column_names):
    # ------------creating empty df to concatinate data--------------------------#
    column_names = ['user', 'tweet_id', 'created_at', 'text']
    alldatadf = pd.DataFrame(columns=column_names)


    #------------Creating path of dir -------------------------------------------#
    fromDirpath = parent_dir+directory+'/'

    #--------------------read files from the directory---------------------------#
    onlyfiles = fileUtils.readFilesFrmDirectory(fromDirpath)

    for i in range(len(onlyfiles)):
        path = onlyfiles[i]

        path = 'data/tweets_' + today + '/' + path

        df = pdUtils.readcsvWithoutHeaders(path)
        #df.reset_index(drop=True, inplace=True)
        # pdUtils.table(df, 'keys')
        # -----------concatinate/Union all stocks-------------------------------#
        #alldatadf = alldatadf.append(df)
        alldatadf = pd.concat([alldatadf, df])




        # non_null_columns = [col for col in alldatadf.columns if alldatadf.loc[:, col].notna().any()]
        # alldatadf = alldatadf[non_null_columns]
        # alldatadf = alldatadf.set_axis(column_names, axis=1, inplace=False)
        #




        # ----------Save Concat Data --------------------------------------------#
        saveConcat(parent_dir, today, alldatadf)


def saveConcat(parent_dir,today,concatDF):
     directory = 'Concat_tweets_' + today
     #-------------------Creating directory to save file-----------------------#
     fileUtils.createDir(parent_dir, directory)

     savePath = os.path.join(parent_dir, directory, 'rawTweets.csv')


     concatDF.to_csv(savePath)




if __name__ == '__main__':


    #pass in the username of the account you want to download
    BrockerNames = ['@moneycontrolcom', '@_groww', '@BT_India','@howtobuybest','@NDTVProfit','@CNBCTV18News','@CNBC_Awaaz',
                    '@ETMarkets','@ETNOWlive','@BloombergQuint','@EconomicTimes','@livemint','@NSEIndia','@BSEIndia',
                    '@stocksbuzzcalls','@hellogaurav','@_soniashenoy','@stockbaat','@darshanvmehta1','@ETNOWlive','@darshanvmehta1',
                    '@IIFLMarkets','@bse_sensex','@BTVI','@anandnst','@brahmachary','@NSE_NIFTY']

    for brockername in BrockerNames:
        tweets = get_all_tweets(brockername,column_names)

