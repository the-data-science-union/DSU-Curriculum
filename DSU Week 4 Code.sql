##Refer to last weeks code to get databases and tables

USE geyserdb
SHOW tables

#Sorting tables
##The "ORDER BY" input will be the primary tool you use to sort your data

SELECT * FROM armspans

##Order by one column
SELECT * FROM armspans ORDER BY height ASC
SELECT * FROM armspans ORDER BY height DESC

##Order by two columns
SELECT * FROM armspans ORDER BY height ASC, armspan DESC

###Like Python, the first column listed will take priority



#Grouping/Summarizing Vairables
##The "GROUP BY" input will be the primary tool for Grouping your data w.r.t a varible
##Usually has the grouping variable, then others with functions on them
##Very clear way to look at you data, review the functions on the video to see all the functions you can use.


SELECT * FROM armspans
SELECT gender, AVG(height), FROM armspans GROUP BY gender #Shows the average by gender



#Putting in a condition
##The "WHERE" input is used here to determine condition used to index certain data

SELECT gender, height FROM armspans WHERE height > 70

##Usually the combination between "WHERE" AND "ORDER BY"

SELECT gender, height FROM armspans WHERE height > 70 ORDER BY height DESC

##Can also use GROUP BY but only for special cases where there are many categories in your category variable.