# https://towardsdatascience.com/stock-market-analysis-in-python-part-1-getting-data-by-web-scraping-cb0589aca178

#page to understand beautifulsoup
# https://www.pluralsight.com/guides/extracting-data-html-beautifulsoup

import numpy as np # linear algebra
import pandas as pd # pandas for dataframe based data processing and CSV file I/O
import requests # for http requests
from bs4 import BeautifulSoup # for html parsing and scraping
import bs4
from fastnumbers import isfloat
from fastnumbers import fast_float
from multiprocessing.dummy import Pool as ThreadPool

import matplotlib.pyplot as plt
import seaborn as sns
import json
from tidylib import tidy_document # for tidying incorrect html

# sns.set_style('whitegrid')
# %matplotlib inline
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

from IPython.core.display import HTML
HTML("<b>Rendered HTML</b>")



#----------Making Http Requests----------------#
# response = requests.get("https://www.moneycontrol.com/stocks/marketstats/onlybuyers.php", timeout=240)
# response.status_code
# response.content

url = "https://www.moneycontrol.com/stocks/marketstats/onlybuyers.php"
url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url, timeout=240)
response.status_code
response.json()

content = response.json()
content.keys()




response = requests.get("https://www.moneycontrol.com/india/stockpricequote/auto-2-3-wheelers/heromotocorp/HHM", timeout=240)
page_content = BeautifulSoup(response.content, "html.parser")
HTML(str(page_content.find("h1")))
print(page_content)
print(str(page_content.find("h1")))


price_div = page_content.find("inprice1 nsecp",attrs={"id":'rel'})
HTML(str(price_div))
content = page_content.find('div', {"class": "inprice1 nsecp"})
print(content)
print(content.text)

percentChange = page_content.find('div', {"class": "nsechange"})
print(percentChange.text)

print("*************************************************************************************")