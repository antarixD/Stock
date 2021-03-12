import pandas  as pd
import ML.utils.pd_file as pdUtils
from pathlib import Path
import ML.utils.fileSystem as fs
from tabulate import tabulate
import ML.utils.datefile as dateUtils
import calendar
import datetime

# Import pandas package
import pandas as pd

# create a dictionary with five fields each
data = {
    'A': ['A1', 'A2', 'A3', 'A4', 'A5'],
    'B': ['B1', 'B2', 'B3', 'B4', 'B5'],
    'C': ['C1', 'C2', 'C3', 'C4', 'C5'],
    'D': ['D1', 'D2', 'D3', 'D4', 'D5'],
    'E': ['E1', 'E2', 'E3', 'E4', 'E5']}

# Convert the dictionary into DataFrame
df = pd.DataFrame(data)
print(df)

# Remove column name 'A'
df = df.drop(['A'], axis=1)
print(df)


def read_in_data(file):
    read_pd = pd.read_csv (file,usecols= ['text'])
    return read_pd


file_path = 'tcs.csv'
out_df = pdUtils.readPd(file_path)
out_df.name = 'Ones'
print ('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ', out_df.name)
print(type(out_df.name))

#print(tabulate(out_df, headers='keys', tablefmt='psql'))
#pdUtils.table(out_df, 'keys')
# import pyexcel as pe
# sheet = pe.Sheet(out_df)
# print(sheet)

path = fs.getFilePathOneDrUp(2)
print('------------------:', path)
sourcePath = str(Path(__file__).parents[1])
print(sourcePath)
outputPath = path + '/ML/data/test.csv'
#pdUtils.savePd(out_df,outputPath)

#df.name = 'Ones'


# today = dateUtils.currentDate()
# last_day = dateUtils.yesterday(today)
# month_days = dateUtils.monthDays()
# last_thirty_day = dateUtils.last_thirty_day(today,month_days)
# # today = date.today()
# # last_day = (today - timedelta(1))
# # last_thirty_day = today - timedelta(30)
# print('last_day: ', last_day)
#
# print('last_thirty_day: ', last_thirty_day)
#
# now = datetime.datetime.now()
# print (calendar.monthrange(2020,8)[1])
# print (calendar.monthrange(now.year, now.month)[1])
#
# print('------', dateUtils.monthDays())