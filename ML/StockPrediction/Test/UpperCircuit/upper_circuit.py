import pandas as pd
from tabulate import tabulate
from datetime import date,timedelta
import itertools
import utils.pd_file as pdUtils
import utils.nseUtils as nseUtils
import numpy as np
import utils.fileSystem as fs
from nsepy import get_history
import utils.pd_file as pdUtils
import utils.fileSystem as fsUtils
import utils.datefile as dateUtils
import StockPrediction.Test.UpperCircuit.upper_circuit_helper as UC_helper
import utils.DfDate as DfDate


path = 'D:/naive bayes/Stocks/registered_companies/MCAP_31032020_0.xlsx'
#---------------reading the name of stocks from the file/excel----------------#
comp_list = pdUtils.readExcel(path)
#-----------------filtering out the null values for column: symbol-------------#
filtered_df = comp_list[comp_list['Symbol'].notnull()]

symb = filtered_df.Symbol
#--------dropping the date index in file-----------------------#
symb = symb.reset_index(drop=True)


today = dateUtils.currentDate()
last_day = dateUtils.yesterday(today)
month_days = dateUtils.monthDays()
last_thirty_day = dateUtils.last_thirty_day(today,month_days)
fourthWeekDate = dateUtils.last_thirty_day(today,8)
thirdWeekDate = dateUtils.last_thirty_day(today,15)
secondWeekDate = dateUtils.last_thirty_day(today,22)





#------------for testing  --> uncomment below line -------------------------#
symb = symb.head(1000)
# print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^: ', type(symb))
# sharev = 'RSSOFTWARE'
# symb = pd.Series(sharev)
print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^: ' , type(symb))
# symb = symb.tail(400)
#*****************************************************************************************


result_list = []
#------------creating empty df to concatinate data--------------------------#
column_names = ["Date ", "Symbol", "Series","Prev Close", "Open", "High","Low ", "Last", "Close","VWAP", "Volume", "Turnover", "Trades", "Deliverable Volume", "%Deliverble", "monthly_growth_%","firstWeek_growth_%", "secondWeek_growth_%", "thirdWeek_growth_%", "fourthWeek_growth_%"]
alldatadf = pd.DataFrame(columns=column_names)
# print(alldatadf)

for ind in symb.index:
     print(symb[ind])
     company_symbol = symb[ind]
     #--------------fetting stock history from NSE-----------------------------#
     stock_fut = nseUtils.stockData(company_symbol,last_thirty_day,last_day)

     #removing any other symbol from data, --> at times nse API gives two stock info with one company symbol
     filter = stock_fut["Symbol"] == company_symbol
     stock_fut.where(filter, inplace=True)
     stock_fut = stock_fut.dropna()

     #------------adding date to df-------------------------#
     stock_fut.reset_index(level=0, inplace=True)
     # pdUtils.table(stock_fut, 'keys')

     #-------------geting max date of the data set fetched-----------------#
     currDate = max(stock_fut.Date)
     #------converting currDate to timeStamp --------------------------#
     currTimestamp = dateUtils.dateToDatetime(currDate)
     #getting second last working day
     yesterday = dateUtils.workingDate(currTimestamp,1)
     DBFyester = dateUtils.workingDate(currTimestamp,2)
     DBFyesteryester = dateUtils.workingDate(currTimestamp,3)

     # getting data from day before yester yester day
     dateCol = "Date"
     dateoutDF = DfDate.dataBwDates(stock_fut, dateCol, DBFyesteryester, currDate)
     #remove null columns from dataframe
     notNullDF = pdUtils.rmvNANrows(dateoutDF)


     # --------------getting data for each day individually ----------------#
     # -----todays Data------#
     todaysData = UC_helper.oneDayData(notNullDF, currDate,dateCol)
     # -----yesterdays Data------#
     yesterData = UC_helper.oneDayData(notNullDF, yesterday,dateCol)
     # -----todays Data------#
     DBFyesterData = UC_helper.oneDayData(notNullDF, DBFyester,dateCol)
     # -----yesterdays Data------#
     DBFyesteryesterData = UC_helper.oneDayData(notNullDF, DBFyesteryester,dateCol)



     # --------calcultiong minus one profit, i.e. profit of today as per yesterday ------#
     TmY = (((todaysData.High - yesterData.High) * 100) / yesterData.High).to_numpy().tolist()
     print('TmY : ', TmY)
     print(type(TmY))

     YmDFY = (((yesterData.High - DBFyesterData.High) * 100) / DBFyesterData.High).to_numpy().tolist()
     print('YmDFY : ', YmDFY)

     DBYmDBYY = (((DBFyesterData.High - DBFyesteryesterData.High) * 100) / DBFyesteryesterData.High).to_numpy().tolist()
     print('DBYmDBYY : ', DBYmDBYY)

     # --------- calculating the no of days of loop ---------------#
     upperCircuitCounter = 0

     if round(TmY[0]) == round(YmDFY[0]):
          upperCircuitCounter = upperCircuitCounter + 1
          if round(YmDFY[0]) == round(DBYmDBYY[0]):
               upperCircuitCounter = upperCircuitCounter + 1
               print(upperCircuitCounter)

     if upperCircuitCounter == 1:
          print('********************************UPPER  **  CIRCUIT*************************************')






     # yesterday = dateUtils.yesterday(currDate)
     # print(yesterday)
     # dayBefYes = dateUtils.dayBeforeYesterday(currDate)
     # print(dayBefYes)
     # # calculating Day before yesterday and day before yesterday yesterday
     # DBFyester = dateUtils.yesterday(yesterday)
     # DBFyesteryester = dateUtils.yesterday(DBFyester)
     # print(DBFyester)
     # print(DBFyesteryester)







#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#      #------------filtering the data as per dates ------------------#
#      #-------------- weekly data---------------------------------#
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
#      #---------- using the latest record to keep data ---------------------#
#      base_df = monthly_data.tail(1)
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
# path = path + '/data'  +'/best_performing_stocks_monthly_'+last_day+'.csv'
#
# pdUtils.savePd(alldatadf,path)
#
#
#
#
#
#
#
