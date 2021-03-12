from nsepy import get_history


#------------------fetch stock data-------------------------#
def stockData(stockName,startDate, endDate):
    stock_fut = get_history(symbol=stockName,
                        start=startDate,
                        end=endDate,
                        futures=False)
    return stock_fut