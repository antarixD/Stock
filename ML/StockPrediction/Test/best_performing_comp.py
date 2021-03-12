import pandas as pd
from tabulate import tabulate
from datetime import date,timedelta
import itertools
import ML.utils.pd_file as pdUtils
import ML.utils.nseUtils as nseUtils
import numpy as np
import ML.utils.fileSystem as fs

from nsepy import get_history
import ML.utils.pd_file as pdUtils
import ML.utils.fileSystem as fsUtils
import ML.utils.datefile as dateUtils
from pandas.tseries.offsets import BDay
from datetime import datetime


path = 'D:/naive bayes/Stocks/registered_companies/MCAP_31032020_0.xlsx'
#---------------reading the name of stocks from the file/excel----------------#
comp_list = pdUtils.readExcel(path)
#-----------------filtering out the null values for column: symbol-------------#
filtered_df = comp_list[comp_list['Symbol'].notnull()]

symb = filtered_df.Symbol
#--------dropping the date index in file-----------------------#
symb = symb.reset_index(drop=True)
print(type(symb))

today = dateUtils.currentDate()
last_day = dateUtils.yesterday(today)
month_days = dateUtils.monthDays()
last_thirty_day = dateUtils.last_thirty_day(today,month_days)
fourthWeekDate = dateUtils.last_thirty_day(today,8)
thirdWeekDate = dateUtils.last_thirty_day(today,15)
secondWeekDate = dateUtils.last_thirty_day(today,22)




def dataBwDates(dataframe, startDate,endDate):
     startDateDf = dataframe.where(dataframe["Date"]>startDate )
     endDateDf = startDateDf.where(startDateDf["Date"] <= endDate)
     return endDateDf

def removeNAN(dataframe,column):
     dataframe = dataframe[dataframe[column].notnull() ]
     return dataframe

def weeklyData(dataframe,startDate,endDate):
     filterdf = dataBwDates(dataframe,startDate,endDate)
     dataframe = removeNAN(filterdf, 'Date')
     return dataframe

#-----------------Adding percentage of average_trades per week with respect to average_trades per month---------------#
def percentTradeGrowth(base_df):
     colName = '1stWeek_Trade(%)'
     percent_growth = (((base_df.firstWeek_TradeAvg - base_df.monthly_TradeAvg)/base_df.monthly_TradeAvg)*100).to_numpy().tolist()
     if len(percent_growth) == 0:
          percent_growth =0
     base_df[colName] = percent_growth
     #
     colName = '2ndWeek_Trade(%)'
     percent_growth = (((base_df.secondWeek_TradeAvg - base_df.monthly_TradeAvg)/base_df.monthly_TradeAvg)*100).to_numpy().tolist()
     if len(percent_growth) == 0:
          percent_growth =0
     base_df[colName] = percent_growth
     #
     colName = '3rdWeek_Trade(%)'
     percent_growth = (((base_df.thirdWeek_TradeAvg - base_df.monthly_TradeAvg)/base_df.monthly_TradeAvg)*100).to_numpy().tolist()
     if len(percent_growth) == 0:
          percent_growth =0
     base_df[colName] = percent_growth
     #
     colName = '4thWeek_Trade(%)'
     percent_growth = (((base_df.fourthWeek_TradeAvg - base_df.monthly_TradeAvg)/base_df.monthly_TradeAvg)*100).to_numpy().tolist()
     if len(percent_growth) == 0:
          percent_growth =0
     base_df[colName] = percent_growth
     return base_df

#--------------------Adding Trading Average columns---------------------#
def avgTradeGrowth(base_df,dataframe):
     colName = dataframe.name + '_TradeAvg'
     #if type(colName) != float:
     percent_growth = dataframe["Trades"].mean()
     percent_growth1 = np.nan_to_num(percent_growth)
     #percent_growth[np.isnan(percent_growth)] = 0


     #percent_growth = int(dataframe["Trades"].mean())#.to_numpy().tolist()
     base_df[colName] = percent_growth1

     return base_df


#----------------Adding high percentage growth columns-----------------------#
def cal(base_df,dataframe):
     colName = dataframe.name + '_growth_%'
     base_price = dataframe.head(1).High
     base_price = base_price.reset_index(drop=True)
     ceiling_price = dataframe.tail(1).High
     ceiling_price = ceiling_price.reset_index(drop=True)
     percent_growth = (((ceiling_price - base_price) / base_price) * 100).to_numpy().tolist()

     if len(percent_growth) == 0:
          percent_growth =0
     base_df[colName] = percent_growth
     #---------------------------getting trage avarage----------------------#
     base_df = avgTradeGrowth(base_df,dataframe)
     return base_df

#------------Deleting the trading average columns----------------------#
def delTradeAvgCol(dataframe):
     column_names = ['firstWeek_TradeAvg','secondWeek_TradeAvg','thirdWeek_TradeAvg','fourthWeek_TradeAvg']
     dataframe = dataframe.drop(column_names, axis = 1)
     #del dataframe[column_names]
     return dataframe










#------------for testing  --> uncomment below line -------------------------#
symb = symb.head(12)
print(':::::::::::::::::::::::::::::::::::::::::::::::::::::::',symb ,',,,,,', type(symb))
# symb = symb.tail(400)
#*****************************************************************************************


result_list = []
#------------creating empty df to concatinate data--------------------------#
column_names = ["Date ", "Symbol", "Series","Prev Close", "Open", "High","Low ", "Last", "Close","VWAP", "Volume", "Turnover", "Trades", "Deliverable Volume", "%Deliverble", "monthly_growth_%","firstWeek_growth_%", "secondWeek_growth_%", "thirdWeek_growth_%", "fourthWeek_growth_%"]
alldatadf = pd.DataFrame(columns=column_names)
print(alldatadf)

for ind in symb.index:
     print(ind, ':-' , symb[ind])
     company_symbol = symb[ind]
     #--------------fetting stock history from NSE-----------------------------#
     stock_fut = nseUtils.stockData(company_symbol,last_thirty_day,last_day)

     #removing any other symbol from data, --> at times nse API gives two stock info with one company symbol
     filter = stock_fut["Symbol"] == company_symbol
     stock_fut.where(filter, inplace=True)
     stock_fut = stock_fut.dropna()

     #------------adding date to df / date was an index till now -------------------------#
     stock_fut.reset_index(level=0, inplace=True)



     #------------filtering the data as per dates ------------------#
     #-------------- weekly data---------------------------------#
     #----------------------Last two days data--------------------------#
     last_days = 3
     last_date = ((today - BDay(last_days)).date())
     lastTwoDays = weeklyData(stock_fut, last_date, last_day)

     pdUtils.table(lastTwoDays, 'keys')

     Stock = ''
     for ind in lastTwoDays.index:
          condition = lastTwoDays[(lastTwoDays['High'] == (lastTwoDays['Close']))]
          stock_fut.where(filter, inplace=True)

          result = lastTwoDays[(lastTwoDays['High'] == (lastTwoDays['Close']))]
          print("-----: ", type(result))
          Stock = (result['Symbol'])
     UpperCircut = Stock.drop_duplicates()
     UpperCircut = UpperCircut.values.tolist()


     print('UpperCircut: ', UpperCircut)
          # if lastTwoDays.High == lastTwoDays.Close:
          #      pdUtils.table(lastTwoDays, 'keys')


     # stock_fut.where(filter, inplace=True)
     # stock_fut = stock_fut.dropna()


        # ---------------END - Last two days data--------------------------#
#      firstWeekData = weeklyData(stock_fut,last_thirty_day,secondWeekDate)
#      secondWeekData = weeklyData(stock_fut, secondWeekDate, thirdWeekDate)
#      thirdWeekData = weeklyData(stock_fut, thirdWeekDate, fourthWeekDate)
#      fourthWeekData = weeklyData(stock_fut, fourthWeekDate, last_day)
#      monthly_data = stock_fut
#      #-----------naming df: to be used as name of columns while saving----------------------#
#      firstWeekData.name = 'firstWeek'
#      secondWeekData.name = 'secondWeek'
#      thirdWeekData.name = 'thirdWeek'
#      fourthWeekData.name = 'fourthWeek'
#      monthly_data.name = 'monthly'
#      monthly_data = stock_fut
#
#
#
#      base_df = monthly_data.head(1)
#
#
#      outdf = cal(base_df,monthly_data)
#      outdf = cal(base_df,firstWeekData)
#      outdf = cal(base_df,secondWeekData)
#      outdf = cal(base_df,thirdWeekData)
#      outdf = cal(base_df,fourthWeekData)
#
#
#      #-----------concatinate/Union all stocks-------------------------------#
#      alldatadf = pd.concat([alldatadf, outdf])
#      #-------------------droping null columns------------------------------#
#      alldatadf = alldatadf.dropna(axis=1)
#      #----------------getting best perfoming 1000 shares as per high over month-------------#
#      alldatadf = alldatadf.sort_values(by=['monthly_growth_%'], ascending=False).head(500)
#      # ----------------getting best perfoming 500 shares as per high over last week-------------#
#      alldatadf = alldatadf.sort_values(by=['fourthWeek_growth_%'], ascending=False).head(100)
#      #-------------------------------VWAP > high-----------------------------------#
#      #alldatadf = alldatadf[alldatadf.Close < alldatadf.VWAP]
#      #-------------getting percentage weekly as per monthly trades----------------#
#
# #-----------------Adding percentage of average_trades per week with respect to average_trades per month---------------#
# alldatadf = percentTradeGrowth(alldatadf)
#
# #------------Deleting the trading average columns----------------------#
# alldatadf = delTradeAvgCol(alldatadf)
#
#
# #------------Deleting additional columns ---------------------------#
# columns = ['Series','Prev Close','Last','Turnover']
# alldatadf = pdUtils.delCol(alldatadf,columns)
# pdUtils.table(alldatadf, 'keys')
#
#
# path = fs.getFilePathOneDrUp(1)
# last_day = last_day.strftime('%d-%m-%Y')
# path = path + '/data'  +'/best_performing_stocks_'+last_day+'.csv'
#
# pdUtils.savePd(alldatadf,path)







