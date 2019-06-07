# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 20:00:51 2019

@author: Nate
"""


import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import os as os
import patsy
import statsmodels.api as sm
import statsmodels.formula.api as smf
from numpy.polynomial.polynomial import polyfit
import scipy as sp
Nate = pd.DataFrame({"Nate":[1,2,3]})

plt.plot(Nate)
plt.show()

Cars = pd.read_csv("cars04.csv")
Cars.columns
Res1 = smf.ols(formula= "Weight ~ CityMPG + HighwayMPG", data=Cars).fit()
print(Res1.summary())
pred_val = Res1.fittedvalues.copy()
true_val = Cars["Weight"].values.copy()

residual = true_val - pred_val

##Residual Plot

fig, ax = plt.subplots(figsize=(6,2.5))
_ = ax.scatter(residual, pred_val)

##Residual plot with density line 
##(Usually the one you wanna go with)

x = residual
y = pred_val

b, m = polyfit(x, y, 1)

plt.plot(x, y, '.')
plt.plot(x, b + m * x, '-')
plt.show()


##Normality Plot

fig, ax = plt.subplots(figsize=(6,2.5))
_, (_,_,r) = sp.stats.probplot(residual,plot=ax,fit=True)
r**2

##Inlfuence Plot

fig, ax = plt.subplots(figsize=(8,6))
fig = sm.graphics.influence_plot(Res1, ax=ax)

##Leverage (Influence) Plot of squared residuals
##Good for observing in terms of absoulute value
##Overall leverage desipte postive or negative error

fig, ax = plt.subplots(figsize=(8,6))
fig = sm.graphics.plot_leverage_resid2(Res1, ax=ax)



