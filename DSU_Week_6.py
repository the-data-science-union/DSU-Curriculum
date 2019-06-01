import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import os as os


Cars = pd.read_csv("cars04.csv")
Cars.head()

Cars.columns


##Alright guys, we introduce you to a new essential package of Data Analytics : Statsmodels
##Statsmodels is one of the two data modeling essential packages in Python (Patsy being the other)
##Go ahead and make sure to get it imported into your program first

import patsy ###Weird story, but statsmodels actually uses the patsy package to produce its models in a sens
             ###Why dont we use patsy then? Cause the coding's easier...

import statsmodels.api as sm


#Simple Linear Regression
##Really straight forward coding...


##Lets say I wanted to run a regression on how City Mileage correlates with  Dealer Cost, see the equation that can predict
##the Dealer cost based off


X = Cars["CityMPG"]   #explanatory variable (the variable that does the explaining)

Y = Cars["DealerCost"]  #response variable (variable that the explaining is in response too)


model = sm.OLS(Y,X) ##To run the regression and build the model

results = model.fit() ##To recieve and give a name to the results from your regression model

##Easy way to check your parameters
results.params

##To see EVERYTHING
print(results.summary())

##Understand this display.... is statistical art
##The coding for a regression is easy but too understand it.. thats what defines a true data analsysts
##WHAT IS IT SAYING, WHAT DOES IT ALL MEAN!

#coef = the coefficent of the variable y = (coef)x

#Pr|t| (p-value) = the proababilty that this one factor defines this variable (Low probabilty means significant [GOOD] results)
                    #Why is this? Due to Students T-Test Edicate
                    #P-Value measures probabilty these results were by random chance
                    #Low P-Value means your test proved "signficant results" and not random results

#R-squared = Coeffiecent of Dtermination, explained variation/total variation. "The variation ratio"
            # Unexplained variation is variation from other varibales

#t (t-statistic) : (xbar-mu0)/(std.error) ,easures to indicate rather of sample mean is the same as the population mean

#Std.error = standard devation of sample size/ sqrt(sample size)

#Conf Int ([0.025 , 0.975]) : #Get a proabable range of the value (im 95% confident the coef will be between...)


#But wheres my constant? we want y = a+Bx not y = Bx
#Add constant :

X = sm.add_constant(X)
X.head()

##Now form a new model

model_2 = sm.OLS(Y,X)

results_2 = model_2.fit()

results_2.params

print(results_2.summary())

##This is the true simple linear regression

#Multi-Linear Regression
##When you want to see more than one explantory variable in correspondence to the response variable


##Now I want to see have much the regression on how to define the Dealer Cost based off city mileage and weight
##Easiest to set x as a Data Frame to all the variables you want as explanatory variables:

X1 = Cars[["CityMPG","Weight"]]
X2 = sm.add_constant(X1)
X2.head()

##Now fit the model

model_3 = sm.OLS(Y,X2)

results_3 = model_3.fit()

results_3.params

print(results_3.summary())


#Regression with Interaction
##For this we denote a new import syntax

import statsmodels.formula.api as smf

###This way is similar to the R Software
###We do all the steps in one go
###You might prefer this way for regular regression as well





#Regular Multi-Regression
##Predict the Dealer Cost by  the City Mileage and Weight of the car
res1 = smf.ols(formula= "DealerCost ~ CityMPG + Weight ", data = Cars).fit()
res1.params
print(res1.summary())

#Regressionn with a Categorical Variable

##Need to import data frame with categorical data
##Simply add C() to the variable
births = pd.read_csv("births.csv")
births.columns
births.head()

##Want to see if we can predict the weight of baby using the race of the mom and dad

catres = smf.ols(formula= "weight ~ C(Racemom) + C(Racedad)", data= births).fit()
catres.params
print(catres.summary())


#Add in interaction factor to formula
res2 = smf.ols(formula= "DealerCost ~ CityMPG + Weight + CityMPG*Weight-1 ", data = Cars).fit()
res2.params


##Interaction is combination of the two variables acting as 1 variable independent of the two.
##This is important because sometimes the combination of two vairbales affects the response varibale differently
##P-Value is the only real signficant statistic it brings

print(res2.summary())


#Transformation on your model
##When we talk about model diagnostics and model vaildity next week,
## sometimes your model won't meet the criteria for a valid model
##Use transformations to "scale and form" the data a new way so it meets the criteria and is valid.
##Typical ones include x^2 and log(x)
##ONLY TRANSFORM EXPLANATORY VARIABLES NOT THE RESPONSE

###Log(x) transformation

res3 = smf.ols(formula= "DealerCost ~ np.log(CityMPG) + np.log(Weight)", data = Cars).fit()
res3.params
print(res3.summary())


###x^2 transformation

res4 = smf.ols(formula= "DealerCost ~ CityMPG**2 + Weight**2", data = Cars).fit()
res4.params
print(res4.summary())


