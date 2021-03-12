from pathlib import Path
import os
import shutil
from os import listdir
from os.path import isfile, join
import numpy as np
from fastnumbers import fast_float
import re


#---------reading the directory up-----------------------#
def getFilePathOneDrUp(index):
    oneDrUpPath = str(Path(__file__).parents[index])
    return oneDrUpPath

#----------------create directory---------------------#
def createDir(parentDir,childDir):
    path = os.path.join(parentDir, childDir)
    #---------------removing the directory if already exists---------------------#
    if os.path.exists(path):
        shutil.rmtree(path)
    os.mkdir(path)

#---------------reading the files in a directory-----------------------------#
def readFilesFrmDirectory(path):
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    return onlyfiles
#--------------String to float conversion----------------------------------#
#We check if input is already float/int then return the same, else remove comma and % and then convert#
def stringToFloat(string):
    if string is None:
        return np.nan
    if type(string)==float or type(string)==np.float64:
        return string
    if type(string)==int or type(string)==np.int64:
        return string
    return fast_float(string.split(" ")[0].replace(',','').replace('%',''),
                      default=np.nan)


#---------------------list of strings--------------------------------------#
def listToString(string_list):
    return list(map(stringToFloat,string_list))


#--------------Removing Multple spaces from within string---------------------#
def remove_multiple_spaces(string):
    if type(string)==str:
        # return '  '.join(string.split(' '))


        _RE_COMBINE_WHITESPACE = re.compile(r"\s+")

        my_str = _RE_COMBINE_WHITESPACE.sub(" ", string).strip()
        my_str = my_str.replace("Add to Watchlist", " Add to Watchlist")
    return my_str



