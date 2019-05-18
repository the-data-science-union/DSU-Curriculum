#Step 4 : Data Exploaration
##These codes serve for a multitude of reasons but the one most impotant is quantifing initial statistics for you data.
##You want to be able to draw samples, get accurate graphs, sort the data. etc...
##You have no real mission for this step, it's the only step that really doesn't have an agenda
##But you want to apply yourself for the sake of exposing the true reality of your data.
##Here are some primary tools to help you while explring you data:
##First in read in some data to illustrate

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import os as os


Cars = pd.read_csv("cars04.csv")
Cars.head()


#Transposing tables
##You can "rotate your table" to accomadate specific values in specific tables
##Wont work if data reshaped contains unenqual rows and columns [no duplicate values]

###Lets say I wanted to index my rows with the columns and columnize by each subject

Cars_T = Cars.T
Cars_T.head()


#Making Dummy Variables
##Helpful when illsutrating the numerierics of Categorical Data
##Here's the Dataframe from the notes

Pets = pd.DataFrame({"Day" : [1,2,3,4], "Pet" : ["Cat","Dog","Dog","Cat"]},)
print(Pets)

Dummies = pd.get_dummies(Pets["Pet"])
Pets1 = pd.concat([Pets,Dummies],axis=1)
###To drop Boolean column
Pets2 = Pets1.drop(["Pet"],inplace=True, axis=1)
print(Pets2)

#Sorting Data
##Most of the sortiung will be applied in SQL, but python contains good sorting tools as well

###Lets say I wanted to put my put my vehicle name in alphabetical order

Cars_Sort1 = Cars.sort_values('Vehicle Name')
print(Cars_Sort1)
###Reverse aplhabetical

Cars_Sort2 = Cars.sort_values('Vehicle Name', ascending=False)
print(Cars_Sort2)

###Same idea for numerical columns with their values
###Can sort two columns at once, python will natrually try to accomodate as "much as possible"
###Will prioirtize first column listed

Cars_Sort3 = Cars.sort_values(['Vehicle Name','CityMPG'], ascending=[True,False])
###Reverse aplhabetical
print(Cars_Sort3)

#Creating Plots/Graphs
##Plots are the most sufficent tool you have to give presentations of your data.
##It's illustations give good insight to the behavior of you data
##Different plots apply to different data
##Usually wanna use box plots and scatterplots for numerical data, historgram for categorical.

###Histograms
n, bins, patches = plt.hist(x=Cars["Width"], bins='auto', facecolor='#0504aa',
                            alpha=0.5)
plt.xlabel('Width Values')
plt.ylabel('Frequency')
plt.title('My Very Own Histogram')
plt.show()

###Scatterplots

###Lets say I wanted to make a scatterplot with engine size as the x variable and CityMPG as the y variable.

plt.scatter(Cars["EngineSize"],Cars["CityMPG"])
plt.xlabel("Engine Size")
plt.ylabel("City Mileage")
plt.title("My Scatterplot")
plt.show()

###Boxplots
###Can be used to solve outliers in your data with re[ect to a single column.
###Best tool to point out outliers alongside leverage points.


###Want to create a boxplot a single category
plt.boxplot(Cars["EngineSize"])
plt.show()

###Create one with multiple groups with respect to another variable
###Data.boxplot(column="Variable 1", by="Grouping Variable")
###Need to have a a categorical variable for the "by" arguement
###Only use this method if you want to see particular values of a variable in groups

#Generate Frequency Tables
##Useful to see exact frequencies between two vairables.
##Works for categorical data mostly.

Births = pd.read_csv("births.csv")
Births.head()

test = Births.groupby(["Gender","Racemom"])
test.size()


#Summarize a varible in your data
##Good for getting initial statisitcs about what is contained inside the variables in your data set

###Numerical
Births['weight'].describe()

###Categorical
Births["Gender"].describe()


#Sampling from your dataset
###Helps you get some random samples from your data

Births.sample(5) #arguement = # of samples.






