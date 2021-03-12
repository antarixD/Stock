#https://towardsdatascience.com/getting-rich-quick-with-machine-learning-and-stock-market-predictions-696802da94fe

from datetime import date
from nsepy import get_history
from pprint import pprint
import json
import argparse



stock_fut = get_history(symbol="CGPOWER",
 start=date(2000, 1, 1),
 end=date(2020, 9, 30),
 futures=False)
stock_fut.head()

stock_fut.to_csv(f'/home/antarix/Desktop/naive bayes/Stocks/Data/CGPOWER.csv')