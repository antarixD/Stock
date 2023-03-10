# https://towardsdatascience.com/stock-market-analysis-in-python-part-1-getting-data-by-web-scraping-cb0589aca178

#page to understand beautifulsoup
# https://www.pluralsight.com/guides/extracting-data-html-beautifulsoup

import numpy as np # linear algebra
import pandas as pd # pandas for dataframe based data processing and CSV file I/O
import requests # for http requests
from bs4 import BeautifulSoup # for html parsing and scraping
import bs4
import re
import pandas as pd
import ML.utils.scrapUtil as scrap
import ML.utils.pd_file as pdUtils
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
from IPython.core.display import HTML
HTML("<b>Rendered HTML</b>")
import ML.utils.fileSystem as fs






#-------------------------reading the table fromthe webpage----------------------------#
#html_data_content = page_content.find('div', {"class": "bsr_table bsr_table930 MT20 PR hist_tbl"})
def readTable(page_content,Div,Class):
    html_data_content = page_content.find(Div, {"class": Class})
    return html_data_content



def dataClean(dataList):
    finalList = []
    for word in dataList:
        m = re.search(r"__\d", word)
        partOne = word[0:m.start()]
        partTwo = word[m.start():len(word)]

        partOne = partOne.replace(",", "").replace("____", " ").replace("___", " ").replace("__", " ").replace("_ _"," ").replace("_", " ")
        partOne = fs.remove_multiple_spaces(partOne)
        partOne = partOne.replace("Add to Watchlist", ",Add to Watchlist")
        partOne = fs.remove_multiple_spaces(partOne)
        partTwo = partTwo.replace(",", "").replace("____", "_").replace("___", "_").replace("__", "_").replace("_ _","_").replace("_", ",")
        strFinal = ("'" + partOne + partTwo + "'")
        strFinal = strFinal.replace(",", "','")
        strList = list(strFinal.split(','))


        # removes the aditional and additional formatted columns
        listExcCounter = 0
        if len(strList) > 41:
            listExcCounter = len(strList) - 41
            newInd = 2 + listExcCounter

            newstr = strList[:2] + strList[newInd:]
            newstr = newstr[:13] + newstr[20:37]
        elif len(strList) == 40:
            newstr = strList[:11] + list(strList[0].split(',')) +strList[11:]
            newstr = newstr[:13] + newstr[20:37]
        else:
            newstr = strList
            newstr = newstr[:13] + newstr[20:37]


            finalList.append(newstr)

    for str in dataList:

        strList = []
        m = re.search(r"__\d", str)
        partOne = str[0:m.start()]
        partTwo = str[m.start():len(str)]
        partOne = partOne.replace(",","").replace("____"," ").replace("___"," ").replace("__"," ").replace("_ _"," ").replace("_"," ")
        partOne = fs.remove_multiple_spaces(partOne)
        partOne = partOne.replace("Add to Watchlist",",Add to Watchlist")
        partOne = fs.remove_multiple_spaces(partOne)
        partTwo = partTwo.replace(",","").replace("____","_").replace("___","_").replace("__","_").replace("_ _","_").replace("_",",")
        strFinal = ("'"+partOne + partTwo+"'")
        strFinal = strFinal.replace(",", "','")
        strList = list(strFinal.split(','))

        #removes the aditional and additional formatted columns
        listExcCounter = 0
        if len(strList) > 41:
            listExcCounter = len(strList) - 41
            newInd = 2 + listExcCounter

            newstr = strList[:2] + strList[newInd:]
            newstr = newstr[:13] + newstr[20:37]
        elif len(strList) == 40:
            newstr = strList[:11] + list(strList[0].split(',')) +strList[11:]
            newstr = newstr[:13] + newstr[20:37]
        else:
            newstr = strList
            newstr = newstr[:13] + newstr[20:37]


            finalList.append(newstr)
        return finalList

def colArrange(df):
    ColRenameList = ['1DayValue', '1DayRaise', '1DayRaise_%']
    ColName = '1stDayValPer'
    df = pdUtils.ColSplit(df, ColName, ColRenameList)
    # -----------dropping the additional columns------------------#
    df = pdUtils.delCol(df, ColName)

    ColRenameList = ['2DayValue', '2DayRaise', '2DayRaise_%']
    ColName = '2thDayValPer'
    df = pdUtils.ColSplit(df, ColName, ColRenameList)
    # -----------dropping the additional columns------------------#
    df = pdUtils.delCol(df, ColName)

    ColRenameList = ['3DayValue', '3DayRaise', '3DayRaise_%']
    ColName = '3thDayValPer'
    df = pdUtils.ColSplit(df, ColName, ColRenameList)
    # -----------dropping the additional columns------------------#
    df = pdUtils.delCol(df, ColName)

    ColRenameList = ['4DayValue', '4DayRaise', '4DayRaise_%']
    ColName = '4thDayValPer'
    df = pdUtils.ColSplit(df, ColName, ColRenameList)
    # -----------dropping the additional columns------------------#
    df = pdUtils.delCol(df, ColName)

    ColRenameList = ['5DayValue', '5DayRaise', '5DayRaise_%']
    ColName = '5thDayValPer'
    df = pdUtils.ColSplit(df, ColName, ColRenameList)
    # -----------dropping the additional columns------------------#
    df = pdUtils.delCol(df, ColName)

    # -----------removing () brackets and quotes from the columns------------------#
    df = pdUtils.ColTrim(df, '1DayRaise_%', '(', ")%'")
    df = pdUtils.ColTrim(df, '2DayRaise_%', '(', ")%'")
    df = pdUtils.ColTrim(df, '3DayRaise_%', '(', ")%'")
    df = pdUtils.ColTrim(df, '4DayRaise_%', '(', ")%'")
    df = pdUtils.ColTrim(df, '5DayRaise_%', '(', ")%'")

    # -----------dropping the additional columns------------------#
    df = pdUtils.delCol(df, 'AverageVolume')
    df = pdUtils.delCol(df, '5D-AvgVol')
    df = pdUtils.delCol(df, '10D-AvgVol')
    df = pdUtils.delCol(df, '30D-AvgVol')
    df = pdUtils.delCol(df, 'DeliveryAvg')
    df = pdUtils.delCol(df, 'DeliveryAvg_3Days')
    df = pdUtils.delCol(df, 'DeliveryAvg_5Days')
    df = pdUtils.delCol(df, 'DeliveryAvg_8Days')

    # -----------removing quotes from the columns------------------#
    df = pdUtils.ColTrim(df, '1DayValue', "'", "_")
    df = pdUtils.ColTrim(df, '2DayValue', "'", "_")
    df = pdUtils.ColTrim(df, '3DayValue', "'", "_")
    df = pdUtils.ColTrim(df, '4DayValue', "'", "_")
    df = pdUtils.ColTrim(df, '5DayValue', "'", "_")
    df = pdUtils.ColTrim(df, 'STOCK', "'", "'")
    df = pdUtils.ColTrim(df, 'NEWS', "'", "'")
    df = pdUtils.ColTrim(df, 'BidQty', "'", "'")
    df = pdUtils.ColTrim(df, 'LastPrice', "'", "'")
    df = pdUtils.ColTrim(df, 'Diff', "'", "'")
    df = pdUtils.ColTrim(df, '%Chg', "'", "'")
    df = pdUtils.ColTrim(df, '5D-AvgVolValue', "'", "'")
    df = pdUtils.ColTrim(df, '10D-AvgVolValue', "'", "'")
    df = pdUtils.ColTrim(df, '30D-AvgVolValue', "'", "'")
    df = pdUtils.ColTrim(df, '5thDay', "'", "'")
    df = pdUtils.ColTrim(df, '4thDay', "'", "'")
    df = pdUtils.ColTrim(df, '3thDay', "'", "'")
    df = pdUtils.ColTrim(df, '2thDay', "'", "'")
    df = pdUtils.ColTrim(df, '1stDay', "'", "'")
    df = pdUtils.ColTrim(df, 'DeliveryAvg_3Days_values', "'", "'")
    df = pdUtils.ColTrim(df, 'DeliveryAvg_5Days_values', "'", "'")
    df = pdUtils.ColTrim(df, 'DeliveryAvg_8Days_values', "'", "'")

    return df


def main():

    #------------------STEP 1----------------------------------------#
    # --------------reading the contents of the page-----------------#
    URL = "https://www.moneycontrol.com/stocks/marketstats/onlybuyers.php"
    response = requests.get(URL, timeout=1000)
    page_content = BeautifulSoup(response.content, "html.parser")
    # HTML(str(page_content.find("h1")))

    # ------------------STEP 2----------------------------------------#
    # -------------------------reading the table content from the webpage----------------------------#
    html_data_content = readTable(page_content,'div',"bsr_table bsr_table930 MT20 PR hist_tbl")

    # ------------------STEP 3----------------------------------------#
    # ------------------------moving the table data to a string---------------------------------#
    petable = scrap.get_table_simple(scrap.get_children(html_data_content)[1], is_table_tag=False)

    headingList = petable[0]
    dataList = petable[1]

    # ------------------STEP 4----------------------------------------#
    # -------------Data cleaning----------------------------------------#
    finalList = []
    for str in dataList:

        strList = []
        m = re.search(r"__\d", str)
        partOne = str[0:m.start()]
        partTwo = str[m.start():len(str)]
        partOne = partOne.replace(",","").replace("____"," ").replace("___"," ").replace("__"," ").replace("_ _"," ").replace("_"," ")
        partOne = fs.remove_multiple_spaces(partOne)
        partOne = partOne.replace("Add to Watchlist",",Add to Watchlist")
        partOne = fs.remove_multiple_spaces(partOne)
        partTwo = partTwo.replace(",","").replace("____","_").replace("___","_").replace("__","_").replace("_ _","_").replace("_",",")
        strFinal = ("'"+partOne + partTwo+"'")
        strFinal = strFinal.replace(",", "','")
        strList = list(strFinal.split(','))

        #removes the aditional and additional formatted columns
        listExcCounter = 0
        if len(strList) > 41:
            listExcCounter = len(strList) - 41
            newInd = 2 + listExcCounter

            newstr = strList[:2] + strList[newInd:]
            newstr = newstr[:13] + newstr[20:37]
        elif len(strList) == 40:
            newstr = strList[:11] + list(strList[0].split(',')) +strList[11:]
            newstr = newstr[:13] + newstr[20:37]
        else:
            newstr = strList
            newstr = newstr[:13] + newstr[20:37]


            finalList.append(newstr)


    # finalList = dataClean(dataList)

    # ------------------STEP 5----------------------------------------#
    #-------------converting the list to dataframe--------------------#
    df = pd.DataFrame.from_records(finalList)
    header = ["STOCK", "NEWS", "BidQty", "LastPrice", "Diff", "%Chg", "AverageVolume", "5D-AvgVol", "5D-AvgVolValue",
              "10D-AvgVol", "10D-AvgVolValue", "30D-AvgVol", "30D-AvgVolValue", "5thDay", "5thDayValPer", "4thDay",
              "4thDayValPer", "3thDay", "3thDayValPer", "2thDay", "2thDayValPer", "1stDay", "1stDayValPer",
              "DeliveryAvg", "DeliveryAvg_3Days", "DeliveryAvg_3Days_values", "DeliveryAvg_5Days",
              "DeliveryAvg_5Days_values", "DeliveryAvg_8Days", "DeliveryAvg_8Days_values"]
    df.columns = header

    #--------------------Data Massaging--------------------#
    df = colArrange(df)

    pathPrifix = "D:/StockData/UpperCircuitData/"
    pathSuffix = "UpperCircuit.csv"
    pdUtils.partitionFileSave(df,pathPrifix,pathSuffix)

    #------------------Step 6-------------------------------#
    #---------------Data Manipulation: dividing data into catogories---------------------#
    #Upper circuit data
    #pd.to_numeric(ID, errors='coerce')
    print(df["1DayRaise_%"])
    print(type(df["1DayRaise_%"]))
    dataframe1UP = pdUtils.dfFilter(df, df["1DayRaise_%"].astype(float) > 0)
    pathSuffix = 'OnlyUpperCircuit.csv'
    pdUtils.partitionFileSave(dataframe1UP, pathPrifix, pathSuffix)

    #Lower circuit data
    dataframeLC = pdUtils.dfFilter(df, df["1DayRaise_%"].astype(float) <= 0)
    pathSuffix = 'OnlyLowerCircuit.csv'
    pdUtils.partitionFileSave(dataframeLC, pathPrifix, pathSuffix)

    #-1- day upper circuit data
    dataframe2UP = pdUtils.dfFilter(dataframe1UP, dataframe1UP["2DayRaise_%"].astype(float) <= 0)
    dataframe2UP = pdUtils.dfFilter(dataframe2UP, dataframe2UP["3DayRaise_%"].astype(float) <= 0)
    dataframe2UP = pdUtils.dfFilter(dataframe2UP, dataframe2UP["4DayRaise_%"].astype(float) <= 0)
    dataframe2UP = pdUtils.dfFilter(dataframe2UP, dataframe2UP["5DayRaise_%"].astype(float) <= 0)
    pathSuffix = '1DayUpperCircuit.csv'
    pdUtils.partitionFileSave(dataframe2UP, pathPrifix, pathSuffix)

    #-2- day upper circuit data
    dataframe3UP = pdUtils.dfFilter(dataframe1UP, dataframe1UP["2DayRaise_%"].astype(float) > 0)
    dataframe3UP = pdUtils.dfFilter(dataframe3UP, dataframe3UP["3DayRaise_%"].astype(float) <= 0)
    dataframe3UP = pdUtils.dfFilter(dataframe3UP, dataframe3UP["4DayRaise_%"].astype(float) <= 0)
    dataframe3UP = pdUtils.dfFilter(dataframe3UP, dataframe3UP["5DayRaise_%"].astype(float) <= 0)
    dataframe3UP = dataframe3UP.sort_values(by=['DeliveryAvg_3Days_values'], ascending=False)
    pathSuffix = '2DayUpperCircuit.csv'
    pdUtils.partitionFileSave(dataframe3UP, pathPrifix, pathSuffix)

    #-3- day upper circuit data
    dataframe3UP = pdUtils.dfFilter(dataframe1UP, dataframe1UP["2DayRaise_%"].astype(float) > 0)
    dataframe3UP = pdUtils.dfFilter(dataframe3UP, dataframe3UP["3DayRaise_%"].astype(float) > 0)
    dataframe3UP = pdUtils.dfFilter(dataframe3UP, dataframe3UP["4DayRaise_%"].astype(float) <= 0)
    dataframe3UP = pdUtils.dfFilter(dataframe3UP, dataframe3UP["5DayRaise_%"].astype(float) <= 0)
    dataframe3UP = dataframe3UP.sort_values(by=['DeliveryAvg_3Days_values'], ascending=False)
    pathSuffix = '3DayUpperCircuit.csv'
    pdUtils.partitionFileSave(dataframe3UP, pathPrifix, pathSuffix)

    #-4- day upper circuit data
    dataframe3UP = pdUtils.dfFilter(dataframe1UP, dataframe1UP["2DayRaise_%"].astype(float) > 0)
    dataframe3UP = pdUtils.dfFilter(dataframe3UP, dataframe3UP["3DayRaise_%"].astype(float) > 0)
    dataframe3UP = pdUtils.dfFilter(dataframe3UP, dataframe3UP["4DayRaise_%"].astype(float) > 0)
    dataframe3UP = pdUtils.dfFilter(dataframe3UP, dataframe3UP["5DayRaise_%"].astype(float) <= 0)
    dataframe3UP = dataframe3UP.sort_values(by=['DeliveryAvg_3Days_values'], ascending=False)
    pathSuffix = '4DayUpperCircuit.csv'
    pdUtils.partitionFileSave(dataframe3UP, pathPrifix, pathSuffix)

    #-5- day upper circuit data
    dataframe3UP = pdUtils.dfFilter(dataframe1UP, dataframe1UP["2DayRaise_%"].astype(float) > 0)
    dataframe3UP = pdUtils.dfFilter(dataframe3UP, dataframe3UP["3DayRaise_%"].astype(float) > 0)
    dataframe3UP = pdUtils.dfFilter(dataframe3UP, dataframe3UP["4DayRaise_%"].astype(float) > 0)
    dataframe3UP = pdUtils.dfFilter(dataframe3UP, dataframe3UP["5DayRaise_%"].astype(float) > 0)
    dataframe3UP = dataframe3UP.sort_values(by=['DeliveryAvg_3Days_values'], ascending=False)
    pathSuffix = '5DayUpperCircuit.csv'
    pdUtils.partitionFileSave(dataframe3UP, pathPrifix, pathSuffix)



if __name__ == "__main__":
    main()  # call main function
