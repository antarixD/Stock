import pandas  as pd
import ML.utils.pd_file as Mpd

def read_in_data(file):
    read_pd = pd.read_csv (file,usecols= ['text'])
    return read_pd

file_path = 'tcs.csv'
out_df = (read_in_data(file_path))
print(out_df)
outputPath = 'ML/Data/test.csv'
Mpd.savePd(out_df,outputPath)