# import utils.datefile as dateUtils
# from datetime import date,timedelta
# import datetime
# import calendar
#
# today = dateUtils.currentDate()
# last_day = dateUtils.yesterday(today)
# month_days = dateUtils.monthDays()
# last_thirty_day = dateUtils.last_thirty_day(today,month_days)
# # print('today',today)
# # print('last_day',last_day)
# # print('month_days',month_days)
# # print('last_thirty_day',last_thirty_day)
#
#
# counter = 0
#
# while counter <= int(month_days):
#
#     lastThirtyDay = today - timedelta(counter)
#     print(lastThirtyDay)
#     counter = counter + 1
#
#
# now = datetime.datetime.now()
# #monthDays = (calendar.monthrange(2020,8)[1])
# monthDays = (calendar.monthrange(now.year, now.month)[1])
# # print(monthDays)
#
#
# abc = 'some string'
# import pandas as pd
# abc_series = pd.Series(abc)
# print (type(abc_series))

import utils.pd_file as pdUtils
from pandas import Timestamp, Series, date_range
import utils.datefile as dateutils
import pandas as pd
import utils.DfDate as DfDate


path = 'C:/Users/HP-1/Desktop/uppercircuitsIn.csv'
out_paths = 'C:/Users/HP-1/Desktop/uppercircuits.csv'
share_data = pdUtils.readcsv(path)
share_data['date'] = pd.to_datetime(share_data['date'], format='%m-%d-%Y')
share_data['date'] = pd.to_datetime(share_data['date'])
share_data['date'] = share_data['date'].dt.date



pdUtils.table(share_data, 'keys')
print(share_data.dtypes )
share_data.to_csv(out_paths, date_format='%Y-%m-%d')

# ------getting current date
currDate = dateutils.currentDate()
print(currDate)
yesterday = dateutils.yesterday(currDate)
print(yesterday)
dayBefYes = dateutils.dayBeforeYesterday(currDate)
print(dayBefYes)
#calculating Day before yesterday and day before yesterday yesterday
DBFyester = dateutils.yesterday(yesterday)
DBFyesteryester = dateutils.yesterday(DBFyester)

# getting data from day before yester yester day
dateCol = "date"
dateoutDF = DfDate.dataBwDates(share_data,"date", DBFyesteryester, currDate)



#---remove null columns from dataframe
notNullDF = pdUtils.rmvNANrows(dateoutDF)
print("_____________________________________________")
pdUtils.table(notNullDF, 'keys')


#------ function to calculate data on one date -------#
def oneDayData(dataframe, date):
    onedayData = dataframe.where(dataframe[dateCol] == date)
    # removing null after filter
    onedayData = pdUtils.rmvNANrows(onedayData)
    # droping the index
    onedayData = onedayData.reset_index(drop=True)
    return onedayData






#--------------getting data for each day individually ----------------#
    #-----todays Data------#
todaysData = oneDayData(notNullDF, currDate)
    # -----yesterdays Data------#
yesterData = oneDayData(notNullDF, yesterday)
    #-----todays Data------#
DBFyesterData = oneDayData(notNullDF, DBFyester)
    # -----yesterdays Data------#
DBFyesteryesterData = oneDayData(notNullDF, DBFyesteryester)


#--------calcultiong minus one profit, i.e. profit of today as per yesterday ------#
TmY = (((todaysData.high - yesterData.high)*100)/yesterData.high).to_numpy().tolist()
print('TmY : ', TmY)
print(type(TmY))

YmDFY = (((yesterData.high - DBFyesterData.high)*100)/DBFyesterData.high).to_numpy().tolist()
print('YmDFY : ', YmDFY)

DBYmDBYY = (((DBFyesterData.high - DBFyesteryesterData.high)*100)/DBFyesteryesterData.high).to_numpy().tolist()
print('DBYmDBYY : ', DBYmDBYY)


#--------- calculating the no of days of loop ---------------#
upperCircuitCounter = 0


# if 0.0 > 0.0:
#     print("Positive number")
# elif 4 == 0:
#     print("Zero")
# else:
#     print("Negative number")
if round(TmY[0]) == round(YmDFY[0]) :
    upperCircuitCounter = upperCircuitCounter + 1
    if round(YmDFY[0]) == round(DBYmDBYY[0]) :
        upperCircuitCounter = upperCircuitCounter + 1
        print(upperCircuitCounter)

if upperCircuitCounter == 1 :
    print('********************************UPPER  **  CIRCUIT*************************************')





# #--------calcultiong minus two profit, i.e. profit of today as per yesterday ------#
# datecol = 'date'
# minusOneProfit = notNullDF.where(notNullDF[datecol] == currDate)
# #removing null after filter
# minusOneProfit = pdUtils.rmvNANrows(minusOneProfit)
# print(minusOneProfit)








