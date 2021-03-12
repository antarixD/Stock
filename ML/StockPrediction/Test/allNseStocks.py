import pandas as pd
import io
import ML.utils.pd_file as pdUtils
import requests
url = 'https://www.nseindia.com/content/indices/ind_nifty50list.csv'
s = requests.get(url).content
print(s)
df = pd.read_csv(io.StringIO(s.decode('utf-8')))
pdUtils.table(df, 'keys')
df.Symbol