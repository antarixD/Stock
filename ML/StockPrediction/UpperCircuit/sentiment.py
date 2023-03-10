import ML.utils.fileSystem as fileUtils
import ML.utils.datefile as dateUtils
import ML.utils.pd_file as pdUtils
import pandas as pd
import nltk
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA


def score(Dataframe):
    results = []
    for headline in Dataframe['desc']:
        pol_score = SIA().polarity_scores(headline) # run analysis
        pol_score['headline'] = headline # add headlines for viewing
        results.append(pol_score)


        Dataframe['Score'] = pd.DataFrame(results)['compound']
        NewsCount = len(Dataframe)
        Dfwith0 = pdUtils.dfFilter(Dataframe,Dataframe['Score']==0)
        DFwith0count = len(Dfwith0)
        Dfwithout0 = pdUtils.dfFilter(Dataframe, Dataframe['Score'] != 0)
        avg_df = Dfwithout0.groupby(['Stock']).mean()
        orderDf= avg_df.sort_values(by='Score', ascending=False, na_position='first').head(100)
        orderDf["NeutralSentiments"]  = DFwith0count
        orderDf["NewsCount"] = NewsCount
    return orderDf


def main():
    dataframe = pdUtils.readcsv("C:/Users/HP-1/Desktop/tcsNews.csv")
    dataframe = dataframe[['Stock', 'desc']]
    newDf = score(dataframe)
    pdUtils.table(newDf, 'keys')


if __name__ == "__main__":
    main()