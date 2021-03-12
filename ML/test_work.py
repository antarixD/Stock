import os
import ML.utils.datefile as dateUtils


today = dateUtils.currentDate()
last_day = dateUtils.yesterday(today)
last_day = last_day.strftime('%d-%m-%Y')


# Directory
directory = 'tweets_'+last_day

# Parent Directory path
parent_dir = "data/"


# Path
path = os.path.join(parent_dir, directory)

# Create the directory
# 'GeeksForGeeks' in
# '/home / User / Documents'
os.mkdir(path)