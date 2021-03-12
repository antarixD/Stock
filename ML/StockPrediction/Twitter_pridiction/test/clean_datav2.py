import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
import tabulate
import datetime
import ML.utils.fileSystem as fileUtils
import ML.utils.datefile as dateUtils
import ML.utils.pd_file as pdUtils





def readConcatTweets(last_day,last_date):

    #------------ reading the concatinated tweet files ------------------------#
    text_df = pd.read_csv ('data/Concat_tweets_'+last_day+'/rawTweets.csv')


    #---------------removing the null columns from df -----------------------#
    alldatadf = pdUtils.revEmptyCol(text_df)

    #-------------redefining the headers/Schema of df ----------------#
    column_names = ["S.No","user","tweet_id", "created_at", "text"]
    alldatadf = alldatadf.set_axis(column_names, axis=1, inplace=False)



    #--------------filter data on basis of date------------------------#
        #----------creating timestamp as per twitter timestamp -----#
    # last_day = last_date.strftime('%Y-%m-%d')
    # start_date = last_day + ' 00:00:01'

        #--------creating filter------------------------------------#
    # after_start_date = alldatadf["created_at"] >= start_date

        #----------using filter to filter data----------------------#
    # alldatadf = alldatadf.loc[after_start_date]


    #-----------------removing the first column S.No-------------------#
    tweetdf = pdUtils.delCol(alldatadf,"S.No")


    return tweetdf


#-----------------converting tweetdf to list-------------------------#
def tweetList(dataframe):
    dataframe = dataframe['text']
    print(dataframe)
    tweetList = dataframe.tolist()
    return tweetList



def stockList(last_day):
    #--------------------------read a file up path---------------------#
    upPath = fileUtils.getFilePathOneDrUp(1)
    #-------------------------creating the stock files path------------#
    upPath = (upPath+'/data/best_performing_stocks_monthly_'+last_day+'.csv')
    #---------------reading stocks file--------------------------------#
    text_df = pd.read_csv(upPath)
    #-----------reading only stocks names in DF------------------------#
    stocksdf = text_df['Symbol']
    #---------------convert df to list of stocks-----------------------#
    stockList = stocksdf.tolist()
    return stockList

stockNames    = ['ALMONDZ', 'SOMICONVEY', 'CALSOFT', 'GROBTEA', 'GOLDTECH', 'AFFLE', 'SORILINFRA', 'REMSONSIND', 'SWELECTES', 'MUTHOOTCAP', 'OMAXAUTO', 'ALLCARGO', 'PUNJABCHEM', 'INSPIRISYS', 'SAFARI', 'GICHSGFIN', 'JMA', 'INDOSTAR', 'NIITLTD', 'PANAMAPET', 'LOTUSEYE', 'THANGAMAYL', 'MUNJALAU', 'WENDT', 'SADBHIN', 'KOTARISUG', 'NBVENTURES', 'LAOPALA', 'CMICABLES', 'EMMBI', 'NEULANDLAB', 'SPAL', 'FINEORG', 'BUTTERFLY', 'ALKYLAMINE', 'ANANTRAJ', 'ADANIENT', 'WABAG', 'BLISSGVS', 'SHANTIGEAR', 'MUNJALSHOW', 'PREMIERPOL', 'BASF', 'INDIAMART', 'SUBROS', 'GNFC', 'SELAN', 'GABRIEL', 'TANLA', 'MANGALAM', 'GENESYS', 'ISFT', 'OPTIEMUS', 'MACPOWER', 'ASHAPURMIN', 'SARDAEN', 'MAHABANK', 'MITTAL', 'DHANBANK', 'KELLTONTEC', 'CESCVENT', 'ROSSELLIND', 'CGPOWER', 'BRFL', 'WINDMACHIN', 'VIKASMCORP', 'PRINCEPIPE', 'VIPCLOTHNG', 'EMAMIREAL', 'KIRIINDUS', 'EXPLEOSOL', 'JAYAGROGN', 'MBLINFRA', 'CREATIVE', 'SPCENET', 'ATFL', 'TGBHOTELS', 'DEEPAKNTR', 'HINDCOMPOS', 'GBGLOBAL', 'ISMTLTD', 'OMKARCHEM', 'GLOBOFFS', 'AKSHOPTFBR', 'ALCHEM', 'A2ZINFRA', 'NELCAST', 'SOMANYCERA', 'PRICOLLTD', 'SINTEX', 'SALSTEEL', 'TALBROAUTO', 'BINDALAGRO', 'DIGISPICE', 'JTEKTINDIA', 'VASWANI', 'ANKITMETAL', 'MANALIPETC', 'GMRINFRA', 'AHLUCONT']


def searchd(dataframe):
    path = '/home/antarix/Desktop/naive bayes/Stocks/registered_companies/MCAP_31032020_0.xlsx'

    comp_list = pdUtils.readExcel(path)

    # ----------------------Test________________________________#
    # ----------------------Test________________________________#
    # ----------------------Test________________________________#
    # ----------------------Test________________________________#
    # ----------------------Test________________________________#
    #----------------------Test________________________________#
    comp_list = comp_list.tail(100)


    filtered_df = comp_list[comp_list['Symbol'].notnull()]
    stockNames = filtered_df['Symbol'].tolist()

    dataframe = dataframe['text'].to_frame()

    tweetLL = dataframe.values.tolist()

    out_list = []

    for stock in stockNames:
        # --------------converting the stock name to upper case and
        # adding spaces before and after for better match -----------#
        org_stock = stock.upper()
        stock = ' ' + org_stock + ' '

        for text in tweetLL:
            #----------------converting the tweets into upper case----------------#
            text = [syllable.upper() for syllable in text]

            for word in text:
                if stock in word:
                    # to remove null objects
                    if type(word) == str:
                        word = (word.replace(',', ''))

                        #  to keep sting as one index in list
                        stock_name = list(org_stock.split("!@#$%^&*"))
                        words = word.split("!@#$%^&*")
                        #converting two lists to list of list
                        concatLL = ([stock_name,words])
                        #appending
                        out_list.append(concatLL)


        out_df = pd.DataFrame(out_list, columns=['Stock','Text'])
    return out_df










   #********************************************************************








# #text_list = text_df.values.tolist()
#
# out_list = []
# for text in text_list:
#     for word in text:
#         if 'TCS' in word:
#             #to remove null objects
#             if type(word) == str:
#                 word = (word.replace(',', ''))
#                 #to keep sting as one index in list
#                 word = list(word.split("!@#$%^&*"))
#                 out_list.append(word)
#
# out_df = pd.DataFrame(out_list, columns =['Text'])
#
#
#
#
# results = []
#
# for headline in out_df['Text']:
#     pol_score = SIA().polarity_scores(headline) # run analysis
#     pol_score['headline'] = headline # add headlines for viewing
#     results.append(pol_score)
#
# results
#
#
#
# out_df['Score'] = pd.DataFrame(results)['compound']
# out_df.to_csv('tcs_clean.csv')
# out_df['group'] = 1
#
#
# # creates a daily score by summing the scores of the individual articles in each day
# final_df = out_df.groupby(['group']).sum()
# print(final_df)
# #print(tabulate(out_df, headers='keys', tablefmt='psql'))
#
#



if __name__ == '__main__':
    today = dateUtils.currentDate()
    last_date = dateUtils.getWorkingDate(5)
    yester_date = dateUtils.yesterday(today)
    yester_date = yester_date.strftime('%d-%m-%Y')
    last_day = last_date.strftime('%d-%m-%Y')
    today = today.strftime('%d-%m-%Y')
    #------Step 1-----------------------Reading the tweets-----------------------#
    tweetdf = readConcatTweets(today,last_date)
    # pdUtils.table(tweetdf.head(100), 'keys')
    # ------Step 2-----------------------Reading the tweets-----------------------#
#    tweetList = tweetList(tweetdf)
    # print(tweetList)
#     # ------Step 3-----------------Reading names of best shares-------------------#
#     stockNames = stockList(last_day)
#     # ------Step 4-----------------Filtering tweets as per best stocks------------#
    StocknTweet = searchd(tweetdf)

    pdUtils.table(StocknTweet, 'keys')