import utils.pd_file as pdUtils

df = pdUtils.readcsv("D:/StockData/MoneyControl/2021/02/08/08-02-2021_NEWS.csv")
df.drop(df.columns[df.columns.str.contains('unnamed', case=False)], axis=1, inplace=True)

pdUtils.table(df,'keys')
#------------main-----------------#
datecol = df['date']
print(type(datecol))