import pandas as pd
from tabulate import tabulate
import pyexcel as pe
import openpyxl

#-------------------read csv to df--------------------------#
def readPd(file):
    read_pd = pd.read_csv (file,usecols= ['text'])
    return read_pd

def readcsv(file):
    read_pd = pd.read_csv (file)
    return read_pd

def readcsvWithoutHeaders(file):
    read_pd = pd.read_csv(file, skiprows=1,header = None).reset_index(drop=True)
    read_pd = read_pd.drop([0], axis=1)
    return read_pd


#--------------------write df as csv------------------------#
def savePd(df,path):
    df.to_csv(path)
    #df.to_csv('tcs.csv')


#----------------------Print df as tabulate -----------------#
def table(df,key):
    #print(tabulate(df, headers='keys', tablefmt='psql'))
    print(tabulate(df, headers=key, tablefmt='psql'))

def pyexcel(df):
    sheet = pe.Sheet(pd)
    print(sheet)


#-----------------Reading a excel--------------------------#
#----------------reading xlx-------------------------------#
def readExcel(path):
    comp_list = pd.read_excel(path)
    return comp_list
#----------------reading xlxs-------------------------------#
# df1=pd.read_excel(
#      os.path.join(APP_PATH, "Data", "aug_latest.xlsm"),
#      engine='openpyxl',
# )


#-------------------Deleting columns----------------------------#
def delCol(dataframe,column_names):
    #column_names = ['firstWeek_TradeAvg', 'secondWeek_TradeAvg', 'thirdWeek_TradeAvg', 'fourthWeek_TradeAvg']
    dataframe = dataframe.drop(column_names, axis=1)
    # del dataframe[column_names]
    return dataframe

#------------removing empty columns -------------------------#
def revEmptyCol(dataframe):
    non_null_columns = [col for col in dataframe.columns if dataframe.loc[:, col].notna().any()]
    dataframe = dataframe[non_null_columns]
    return dataframe

#------------removing na row -------------------------#
def rmvNANrows (dataframe):
    nonNANDF = dataframe.dropna()
    return nonNANDF


#-------------spliting the colum into multiple-------------------------#
def ColSplit(dataFrame,ColName,ColRenameList):
    # df[['1DayValue','1DayRaise','1DayRaise_%']] = df['1stDayValPer'].str.split(expand=True)
    dataFrame[ColRenameList] = dataFrame[ColName].str.split(expand=True)
    return dataFrame

#-----------------------Ltrim and Rtrim from columns----------------------#
def ColTrim(dataframe, colName, lTrim, rTrim):
    #df['1DayRaise_%'] = df['1DayRaise_%'].map(lambda x: x.lstrip('(').rstrip(")%'"))
    dataframe[colName] = dataframe[colName].map(lambda x: x and x.lstrip(lTrim).rstrip(rTrim))
    dataframe[colName] = dataframe[colName].map(lambda x: x and x.lstrip(" ").rstrip(" "))
    return dataframe


#---------Save partition files-----------------------------------------------#
#pathPrifix =  "D:/StockData/UpperCircuitData/"
#pathSuffix =  "UpperCircuit.csv"
def partitionFileSave(dataFrame,pathPrifix,pathSuffix):
    import utils.datefile as dateUtil
    todayDate = dateUtil.currentDate()
    year = todayDate.year
    date = todayDate.day
    month = todayDate.month
    # ----------formatting date, month, and year and converting them to string -----------------#
    month = '{:02}'.format(month)
    year = '{:04}'.format(year)
    date = '{:02}'.format(date)
    # converting today into string
    today = todayDate.strftime('%d-%m-%Y')
    path = (pathPrifix + year + '/' + month + '/' + date + '/' + today + '_'+pathSuffix)
    #creating the directories where the path has to be saved
    import os
    if not os.path.exists(pathPrifix + year + '/' + month + '/' + date):
        os.makedirs(pathPrifix + year + '/' + month + '/' + date)
    #saving the file in the directories created
    print(path)
    savePd(dataFrame, path)




#-----------------converting df to list-------------------------#
def dfToList(dataframe,column):
    dataframe = dataframe[column]
    tweetList = dataframe.tolist()
    return tweetList


#--------------------dataframe for filter--------------------------------#
#filter ----> DataFrame["column_name"] > value  --->  DataFrame["1DayRaise_%"]>0
def dfFilter(DataFrame, filter):
    dataframeUP = DataFrame.where(filter)
    dataframeUP.reset_index(drop=True, inplace=True)
    dataframeUP = rmvNANrows(dataframeUP)
    dataframeUP.reset_index(drop=True, inplace=True)
    dataframeUP.drop(dataframeUP.columns[dataframeUP.columns.str.contains('unnamed', case=False)], axis=1, inplace=True)
    return dataframeUP

