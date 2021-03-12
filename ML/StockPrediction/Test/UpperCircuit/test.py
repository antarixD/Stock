import datetime
# BDay is business day, not birthday...
from pandas.tseries.offsets import BDay

today = datetime.datetime.today()
print(today)
print(type(today))
wday = today - BDay(2)
print(wday)
wdate = wday.date()
print(wdate)
print(type(wdate))