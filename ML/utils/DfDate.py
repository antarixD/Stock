


#------fetch the data from 'dataframe', where date column is 'datecol' and date rane is 'StartDate'
#----- to 'endDate'-------------------------------------------------------------------------------#
def dataBwDates(dataframe, datecol, startDate, endDate):
    startDateDf = dataframe.where(dataframe[datecol] >= startDate)
    endDateDf = startDateDf.where(startDateDf[datecol] <= endDate)
    return endDateDf