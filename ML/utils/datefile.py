import datetime
from datetime import date,timedelta
import calendar
from pandas.tseries.offsets import BDay



def currentDate():
    today = date.today()
    return today

def yesterday(today):
    last_day = (today - timedelta(1))
    return last_day

def dayBeforeYesterday(today):
    last_day = (today - timedelta(2))
    return last_day

#function to get last n date
def dateBeforeNDays(today,noOfDays):
    last_day = (today - timedelta(noOfDays))
    return last_day

#function to chnage the dateformat
#dateFormatChange(currentDate,'%m/%d/%Y')
def dateFormatChange(date,format):
    changedDate = date.strftime(format)
    return changedDate

def last_thirty_day (today,monthDays):
    lastThirtyDay = today - timedelta(monthDays)
    return lastThirtyDay

def monthDays():
    now = datetime.datetime.now()
    #monthDays = (calendar.monthrange(2020,8)[1])
    monthDays = (calendar.monthrange(now.year, now.month)[1])
    return monthDays

#-----------------get date as per number of working days ------------#
def getWorkingDate(noOfDays):
    today = currentDate()
    WorkingDate = (today - BDay(noOfDays))
    return WorkingDate

#-------------------get series of dates from today till last number of days in the current month ------------#
def getDateSeries(startDate, daysInMonth):
    counter = 0
    while counter <= int(daysInMonth):
        dateSeries = startDate - timedelta(counter)
        counter = counter + 1
        return dateSeries

#-------------Fetch n-1 working date -------------#
def workingDate(currDate,day):
    # today = datetime.datetime.today()
    wday = currDate - BDay(day)
    wdate = wday.date()
    return wdate

#----------------convert date to datetime------------#
def dateToDatetime(currDate):
    from datetime import datetime
    dt = datetime.combine(currDate, datetime.min.time())
    return dt