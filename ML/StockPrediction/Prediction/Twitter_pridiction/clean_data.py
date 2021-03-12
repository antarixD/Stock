import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
import tabulate



text_df = pd.read_csv ('tcs.csv',usecols= ['text'])

text_list = text_df.values.tolist()

out_list = []
for text in text_list:
    for word in text:
        if 'TCS' in word:
            #to remove null objects
            if type(word) == str:
                word = (word.replace(',', ''))
                #to keep sting as one index in list
                word = list(word.split("!@#$%^&*"))
                out_list.append(word)

out_df = pd.DataFrame(out_list, columns =['Text'])




results = []

for headline in out_df['Text']:
    pol_score = SIA().polarity_scores(headline) # run analysis
    pol_score['headline'] = headline # add headlines for viewing
    results.append(pol_score)

results



out_df['Score'] = pd.DataFrame(results)['compound']
out_df.to_csv('tcs_clean.csv')
out_df['group'] = 1


# creates a daily score by summing the scores of the individual articles in each day
final_df = out_df.groupby(['group']).sum()
print(final_df)
#print(tabulate(out_df, headers='keys', tablefmt='psql'))


