import pandas as pd
from tabulate import tabulate
from datetime import date,timedelta
import itertools
# import ML.utils.pd_file as pdUtils
# import ML.utils.nseUtils as nseUtils
import utils.pd_file as pdUtils
import utils.nseUtils as nseUtils
import numpy as np
# import ML.utils.fileSystem as fs
import utils.fileSystem as fs


from nsepy import get_history
# import ML.utils.pd_file as pdUtils
# import ML.utils.fileSystem as fsUtils
# import ML.utils.datefile as dateUtils
import utils.pd_file as pdUtils
import utils.fileSystem as fsUtils
import utils.datefile as dateUtils


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
     # print('adding Trading Average columns')
     colName = dataframe.name + '_TradeAvg'
     #if type(colName) != float:
     percent_growth = dataframe["Trades"].mean()
     percent_growth1 = np.nan_to_num(percent_growth)
     #percent_growth[np.isnan(percent_growth)] = 0
     #percent_growth = int(dataframe["Trades"].mean())#.to_numpy().tolist()
     base_df[colName] = percent_growth1
     #pdUtils.table(base_df, 'keys')
     return base_df


#----------------Adding high percentage growth columns-----------------------#
def cal(base_df,dataframe):
     #pdUtils.table(dataframe, 'keys')
     colName = dataframe.name + '_growth_%'
     #geting the highest price of first and last entry of the week
     base_price = dataframe.head(1).High
     base_price = base_price.reset_index(drop=True)
     ceiling_price = dataframe.tail(1).High
     ceiling_price = ceiling_price.reset_index(drop=True)
     #calculating the percentage growth in high price over last week
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
symb = symb.head(100)
# symb = symb.tail(400)
#*****************************************************************************************


result_list = []
#------------creating empty df to concatinate data--------------------------#
column_names = ["Date ", "Symbol", "Series","Prev Close", "Open", "High","Low ", "Last", "Close","VWAP", "Volume", "Turnover", "Trades", "Deliverable Volume", "%Deliverble", "monthly_growth_%","firstWeek_growth_%", "secondWeek_growth_%", "thirdWeek_growth_%", "fourthWeek_growth_%"]
alldatadf = pd.DataFrame(columns=column_names)
print('column_names : ', alldatadf)

for ind in symb.index:
     print(symb[ind])
     company_symbol = symb[ind]
     #--------------fetching stock history from NSE-----------------------------#
     stock_fut = nseUtils.stockData(company_symbol,fourthWeekDate,today)


     #removing any other symbol from data, --> at times nse API gives two stock info with one company symbol
     filter = stock_fut["Symbol"] == company_symbol
     stock_fut.where(filter, inplace=True)
     stock_fut = stock_fut.dropna()

     #------------adding date to df-------------------------#
     stock_fut.reset_index(level=0, inplace=True)




     # #------------filtering the data as per dates ------------------#
     # #-------------- weekly data---------------------------------#
     # firstWeekData = weeklyData(stock_fut,last_thirty_day,secondWeekDate)
     # secondWeekData = weeklyData(stock_fut, secondWeekDate, thirdWeekDate)
     # thirdWeekData = weeklyData(stock_fut, thirdWeekDate, fourthWeekDate)
     # fourthWeekData = weeklyData(stock_fut, fourthWeekDate, today)
     # monthly_data = stock_fut

     # #-----------naming df: to be used as name of columns while saving----------------------#
     # firstWeekData.name = 'firstWeek'
     # secondWeekData.name = 'secondWeek'
     # thirdWeekData.name = 'thirdWeek'
     # fourthWeekData.name = 'fourthWeek'
     # monthly_data.name = 'monthly'
     monthly_data = stock_fut
     monthly_data.name = 'Week'


     #---------- using the latest record to keep data ---------------------#
     base_df = monthly_data.tail(1)
     #pdUtils.table(base_df, 'keys')


     outdf = cal(base_df,monthly_data)
     #print('------------data after cal --------------------')

     #outdf = cal(base_df,firstWeekData)
     # outdf = cal(base_df,secondWeekData)
     # outdf = cal(base_df,thirdWeekData)
     # outdf = cal(base_df,fourthWeekData)


     #-----------concatinate/Union all stocks-------------------------------#
     #print("------------concatinate/Union all stocks--------------")
     alldatadf = pd.concat([alldatadf, outdf])
     #pdUtils.table(alldatadf, 'keys')
     #-------------------droping null columns------------------------------#
     #print("------------droping null columns--------------")
     alldatadf = alldatadf.dropna(axis=1)
     #----------------getting best perfoming 1000 shares as per high over month-------------#
     alldatadf = alldatadf.sort_values(by=['Week_growth_%'], ascending=False).head(50)
     # # ----------------getting best perfoming 500 shares as per high over last week-------------#
     # alldatadf = alldatadf.sort_values(by=['fourthWeek_growth_%'], ascending=False).head(100)
     #-------------------------------VWAP > high-----------------------------------#
     #alldatadf = alldatadf[alldatadf.Close < alldatadf.VWAP]
     #-------------getting percentage weekly as per monthly trades----------------#

#-----------------Adding percentage of average_trades per week with respect to average_trades per month---------------#
#alldatadf = percentTradeGrowth(alldatadf)

#------------Deleting the trading average columns----------------------#
#alldatadf = delTradeAvgCol(alldatadf)


#------------Deleting additional columns ---------------------------#
columns = ['Series','Prev Close','Last','Turnover']
alldatadf = pdUtils.delCol(alldatadf,columns)
pdUtils.table(alldatadf, 'keys')



path = fs.getFilePathOneDrUp(1)
today = today.strftime('%d-%m-%Y')
path = path + '/data'  +'/best_performing_weekly_'+today+'.csv'

pdUtils.savePd(alldatadf,path)







