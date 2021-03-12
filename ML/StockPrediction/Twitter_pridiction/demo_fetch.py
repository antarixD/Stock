import tweepy
from tweepy import OAuthHandler

# # Your Twittter App Credentials
# consumer_key = "XXXXXXXXXXX"
# consumer_secret = "YYYYYYYYYYY"
# access_token = "ZZZZZZZZZZZZZZZZZZ"
# access_token_secret = "CCCCCCCCCCCCCCCCCC"

#Twitter API credentials
consumer_key = "4cP3SXcVQYbsm6XgU4m1SufRe"
consumer_secret = "rgeZajux9kb20LJ5l03EDqErrf9R4GXjFOFV4X6J8HGEiOaIuL"
access_token = "1296554839019646976-DktsUlS9TRuI7L7lpithjGU5tdtq5s"
access_token_secret = "GMtArRyG8jyTuHef9TB75TxHNZDVyM0Pxa0XpPQJ0dI6j"

# Calling API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Provide the keyword you want to pull the data e.g. "Python".
keyword = "TCS"

# Fetching tweets
tweets = api.search(keyword, count=10, lang='en', exclude='retweets',
                    tweet_mode='extended')

for item in tweets:
    print(item)