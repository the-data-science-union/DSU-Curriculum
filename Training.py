import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import os as os
### to manually install : -m pip install SomePackage



#Finding Work Directory

os.getcwd()

#Making Data Frames and Matrices
k1 = pd.DataFrame({"Nate" : [1,5,6,7], "Barrett" : [4,2,3,1]}, index=["h","e","l","p"])
print(k1["Nate"])
print(k1["Nate"][0])
hf = np.array([(1,2,3,4),(5,6,7,8)],)
print(hf)
print(hf[0])
print(hf[0,1])


#Reading in Data
##Other ways such as using module "csv" but this is standard

Cars = pd.read_csv("cars04.csv")
Cars.head()


#Cleansing Data
##First check for interpretation and inconsistencies manually first!!
##Usually applies to data entries when they don't have a certain value or a value is inconsistent with the rest
##
data = pd.Series([1, np.nan, 'hello', None])

##Fixing Null Values
###Finding null values

data.isnull()
data[data.notnull()]

##Removing Null Values
###Be careful with this, you don't wanna get ahead of yourself

data.dropna()

df = pd.DataFrame([[1,      np.nan, 2],
                   [2,      3,      5],
                   [np.nan, 4,      6]])
df

df.dropna()
df.dropna(axis='columns')
df[3] = np.nan
df
df.dropna(axis='columns', how='all')


##Filling NA Values
###This is a much preferred method to dealing with NA values

data = pd.Series([1, np.nan, 2, None, 3], index=list('abcde'))
data

data.fillna(0)
###forward-fill
data.fillna(method='ffill')
### back-fill
data.fillna(method='bfill')
###On dataframes
df.fillna(method='ffill', axis=1)



##Fixing redundent Whitespace
###Usually, applies to columns more than anything to keep uniform syntax
###White spaces can cause errors and bugs when indexing for analysis
###Errors in strings if data frame has white space between characters in strings in some languages can ouput as NA

my_string = "  This   sentence    contains many redundant    whitespaces    !!!  "
my_string_1 = my_string.strip()
print(my_string_1)
my_string_2 = my_string.rstrip()
print(my_string_2)
my_string_3 = my_string.lstrip()
print(my_string_3)
import re
my_string_4 = re.sub(" +", " ",my_string)
print(my_string_4)
my_string_5 = my_string.replace(" ", "")
print(my_string_5)


##Application to dataframes
###Usually wanna use this set up when reading in "raw" data

#pd.read_table("Name of file.[format]", sep=r",", Names : [] )

##Does anyone have a text file?

Data2 = pd.read_table("data.csv", sep=r',', names=["Year", "Make", "Model", "Description"])


##Using Converters
##Converters are applied objects of the read_[] method of pandas, can give special read functions to lines
##Helps make time when column has same problem with every entry

print(Data2) ###observe how the entries are not uniformly spaced.

def strip(text):
    try:
        return text.strip()
    except AttributeError:
        return text

def make_int(text):
    return int(text.strip('" '))

table = pd.read_table("data.csv", sep=r',',
                      names=["Year", "Make", "Model", "Description"],
                      converters = {'Description' : strip,
                                    'Model' : strip,
                                    'Make' : strip,
                                    'Year' : make_int})
print(table)

##Noticed how it didn't fix everything...






