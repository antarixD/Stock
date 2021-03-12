#https://medium.com/@randerson112358/stock-market-sentiment-analysis-using-python-machine-learning-5b644f151a3e

import pandas as pd
import numpy as np
from textblob import TextBlob
import re
import nltk
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Load the data
from google.colab import files
files.upload()
