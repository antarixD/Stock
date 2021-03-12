# https://medium.com/analytics-vidhya/googlenews-api-live-news-from-google-news-using-python-b50272f0a8f0

from GoogleNews import GoogleNews
from newspaper import Article
from newspaper import Config
import pandas as pd
import nltk
#config will allow us to access the specified url for which we are #not authorized. Sometimes we may get 403 client error while parsing #the link to download the article.
nltk.download('punkt')
import utils.pd_file as pdUtils
import UpperCircuitScrap
import utils.datefile as dateUtils
import StockPrediction.UpperCircuit.sentiment as sentiment

#----------------------getting the date range----------------------------#
#returns current date and 5 days back both in string format and MM/DD/YYYY format
def dateBrackets():
    currentDate = dateUtils.currentDate()
    today = dateUtils.dateFormatChange(currentDate, '%m/%d/%Y')
    lastDate = dateUtils.dateBeforeNDays(currentDate, 3)
    lastDate = dateUtils.dateFormatChange(lastDate,'%m/%d/%Y')
    return today,lastDate


def googleNews(stockList,OutDF):
    # defining empty df
    newsDf = pd.DataFrame()
    #loop for each stck in the list of stocks
    for stockName in stockList:
        print(stockName)
        print("----------------------------------------------------")
        #defining the brousers, which are agents here
        user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
        config = Config()
        config.browser_user_agent = user_agent
        presentday, LastDate = dateBrackets()
        #getting the news between the dates, LsatDate is start date and present date is Current date
        googlenews=GoogleNews(start=LastDate,end=presentday)
        # googlenews=GoogleNews(start=LastDate,end='01/21/2021')
        googlenews.search(stockName)
        result=googlenews.result()

        # to get multiple pages of google search
        for i in range(2,5):
            googlenews.getpage(i)
            result=googlenews.result()
            newsDf=pd.DataFrame(result)
            newsDf["Stock"] = stockName
        if len(result)  == 0:
            continue
        else:
            newsDf = newsDf[['Stock', 'desc']]
            # pdUtils.savePd(newsDf, "C:/Users/HP-1/Desktop/tcsNews.csv")
            newsDf = sentiment.score(newsDf)
            OutDF = OutDF.append(newsDf)

    return OutDF

def runLocal():
    stockList = ['Ginni Filaments', 'EngineersInd', 'Subex', 'Hikal', 'Hinduja Global']
    #---------get GoogleNews--------------#
    # defining empty df
    OutNewsDf = pd.DataFrame()
    NewsDf = googleNews(stockList,OutNewsDf)
    pdUtils.table(NewsDf,'keys')
    return NewsDf

def runcluster():
    # runCluster = UpperCircuitScrap.main()
    runCluster = pdUtils.readcsv("D:/StockData/UpperCircuitData/2021/02/08/08-02-2021_2DayUpperCircuit.csv")
    runClusterStocks = runCluster[["STOCK"]]
    print(type(runClusterStocks))

    # ---------------removing the null columns from df -----------------------#
    alldatadf = pdUtils.revEmptyCol(runClusterStocks)
    #--------------removing NAN columns--------------------------------------#
    alldatadf = pdUtils.rmvNANrows(alldatadf)
    #--------------converting df to list------------------------------------#
    stockList = pdUtils.dfToList(alldatadf,"STOCK")
    print(stockList)

    #*************************************************************************#
    #---------get GoogleNews--------------#
    # defining empty df
    OutNewsDf = pd.DataFrame()
    NewsDf = googleNews(stockList,OutNewsDf)
    pdUtils.table(NewsDf, 'keys')
    return NewsDf



def main():
    #---------------step one : get stocks name------------------------------#
    # uncommnet to run in local
    #df = runLocal()
    # uncommnet to run in cluster
    df = runcluster()

    #saving the file into partition
    pathPrifix =  "D:/StockData/UpperCircuitData/Sentiments/"
    pathSuffix =  "SentimentsUpperCircuit.csv"
    pdUtils.partitionFileSave(df,pathPrifix,pathSuffix)



if __name__ == "__main__":
    main() #call main function
