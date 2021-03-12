import numpy as np # linear algebra
import pandas as pd # pandas for dataframe based data processing and CSV file I/O
import requests # for http requests
from bs4 import BeautifulSoup # for html parsing and scraping
import bs4
import utils.fileSystem as fs
import utils.datefile as dateUtil
from datetime import date,timedelta
import utils.pd_file as pdUtils
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
from IPython.core.display import HTML
HTML("<b>Rendered HTML</b>")




# #----------Get URL page Data----------------#
def ScrapNEWS(URL, finaldf):
    print(URL)

    #response = requests.get("https://www.moneycontrol.com/news/business/stocks", timeout=240)
    response = requests.get(URL, timeout=240)
    page_content = BeautifulSoup(response.content, "html.parser")
    # HTML(str(page_content.find("h1")))
    table = page_content.html.find_all('ul')

    #get all the news from ul on the page
    row_data = list()
    for element in table:
        # text = element.text.strip().replace("\n", "_")
        text = element.text.strip()
        text = fs.remove_multiple_spaces(text)
        row_data.append(text)
    newsString = max(row_data, key=len)
    # print(newsString)

    #get dates for last 15 days in dynamic way
    DateList = dateList()

    finaldf = dataReArrange(DateList,newsString,finaldf)
    return finaldf

#---------------get dynaimc date range---------------------#
#----------------------------------------------------------#
#this returns the list of dates of last 30 days in list
def dateList():
    today = dateUtil.currentDate()
    counter = 30
    monthDays = 0
    dateList = []

    for counter in range(30):
        dates = today - timedelta(monthDays)
        monthDays = monthDays + 1
        dates = dateUtil.dateFormatChange(dates, '%B %d')
        dateList.append(dates)
    return dateList


def dataReArrange(dateList,newsString,finaldf):

    for date in dateList:
        NewsListListL = []
        # replacing he old dates with current dates
        newsString = newsString.replace(date, "***###" + date)
        newsList = list(newsString.split("***###"))
        NewsListList = []
        for news in newsList:
            news = news.replace('IST','IST ***###')
            newsList = list(news.split("***###"))
            if len(newsList)==2:
                NewsListList.append(newsList)
        NewsListListL.append(NewsListList)
        #removing a layer od list from list os list of list
        #to convert it to list of list
        flat_list = [item for sublist in NewsListListL for item in sublist]


    df = pd.DataFrame(flat_list)
    finaldf = pd.concat([df,finaldf])
    return finaldf




def main():
    #creating the final df, it captures the data from all pages
    finaldf = pd.DataFrame()

    # ----------Genrating Dynamic URL----------------#
    #setting counter to 5 to fetch data of five pages of news
    counter = 5
    for counter in range(5):
        print(counter)
        if counter == 0:
            URL = "https://www.moneycontrol.com/news/business/stocks/"
            #get the df of news
            #ScrapNEWS()
            finaldf = ScrapNEWS(URL,finaldf)
        else:
            URL = "https://www.moneycontrol.com/news/business/stocks/page-" + str(counter)
            #get the df of news
            finaldf = ScrapNEWS(URL,finaldf)
    pdUtils.table(finaldf,"keys")
    # removing null rows from df
    finaldf = pdUtils.rmvNANrows(finaldf)
    # defining the columns
    finaldf.columns = ['date', 'NEWS']


    #--------------------Saving file into partition--------------------#
    pathPrifix = "D:/StockData/MoneyControl/"
    pathSuffix = "NEWS.csv"
    pdUtils.partitionFileSave(finaldf,pathPrifix,pathSuffix)


if __name__ == "__main__":
    main()  # call main function
