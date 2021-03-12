import pandas as pd
# import nltk
# from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
# import tabulate
# import datetime
# import ML.utils.fileSystem as fileUtils
# import ML.utils.datefile as dateUtils
# import ML.utils.pd_file as pdUtils
#
# today = dateUtils.currentDate()
# last_date = dateUtils.yesterday(today)
# last_day = last_date.strftime('%d-%m-%Y')
# # --------------------------read a file up path---------------------#
# upPath = fileUtils.getFilePathOneDrUp(1)
# # -------------------------creating the stock files path------------#
# upPath = (upPath +'/data/best_performing_stocks_monthly_' +last_day +'.csv')
# # ---------------reading stocks file--------------------------------#
# text_df = pd.read_csv(upPath)
# # -----------reading only stocks names in DF------------------------#
# stocksdf = text_df['Symbol'].to_frame()
# print(stocksdf)
# # ---------------convert df to list of stocks-----------------------#
# stockList = stocksdf.values.tolist()
# print(stockList)
#
#
# a, b, c, _, _ = csv_to_dataset(csv_file_path)

dataname = ['name']
data = ["xfegerg erhrtn wgerh qghehe"]

newL = [dataname,data]
df = pd.DataFrame(newL)


print(newL)

data = [[0, 1, 2],[3, 4, 5]]
df = pd.DataFrame(data)
print(df)


import pandas as pd

df = pd.DataFrame({
    'A': [['a', 'b', 'c'], ['A', 'B', 'C']]
    })

# Out[8]:
#            A
# 0  [a, b, c]
# 1  [A, B, C]

df['Joined'] = df.A.apply(', '.join)

print(df)

df['Joined'] = df['A'].dropna('A').apply(lambda x: ', '.join(map(str, x)))
print(df)