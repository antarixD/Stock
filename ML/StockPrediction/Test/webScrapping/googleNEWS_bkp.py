# https://medium.com/analytics-vidhya/googlenews-api-live-news-from-google-news-using-python-b50272f0a8f0

from GoogleNews import GoogleNews
from newspaper import Article
from newspaper import Config
import pandas as pd
import nltk
#config will allow us to access the specified url for which we are #not authorized. Sometimes we may get 403 client error while parsing #the link to download the article.
nltk.download('punkt')
import utils.pd_file as pdUtils

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
config = Config()
config.browser_user_agent = user_agent
googlenews=GoogleNews(start='01/15/2021',end='01/20/2021')
googlenews.search('TCS')
result=googlenews.result()
df=pd.DataFrame(result)
print(df.head())

df_1 = pd.DataFrame()
for i in range(2,10):
    googlenews.getpage(i)
    result=googlenews.result()
    df_1=pd.DataFrame(result)
print(df_1)
pdUtils.table(df_1,'keys')
pdUtils.savePd(df_1,"C:/Users/HP-1/Desktop/tcsNews.csv")
