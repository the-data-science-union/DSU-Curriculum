#Exporting Tables using wizard

CREATE database geyserdb;
USE geyserdb;
CREATE table geyser (
time INT NOT NULL PRIMARY KEY ,
eruption FLOAT NOT NULL,
inter INT NOT NULL,
CATEGORY INT NOT NULL
);

INSERT INTO geyser VALUE
(1, 8.2, 11,4),
(745, 6.4, 10 ,5)

SELECT * FROM geyser

###Now go the bottom of the bottom left of your screen below "Schemas" 
###click on the arrow pointing down right next to the name of your database.
###now click on the arrow next to "Tables"
###Now right click on the name of your database and go to "Table Data Export Wizard"
###The instructions to export a table are pretty straightfoward.
###Email us if you have quesitons.




#Importing Tables using Wizard
###Same thing as last time, this time using "Table Data Import Wizard"
###Just hit the browse button and click on your dataset
### Create a new table, you can create a new database if you want to put it in.
###One little trick to this when you hit the window titled "COnfigure import Settings"...
### Uncheck the blank row below "Source Column", it can sometimes cause unwanted errors.

SHOW TABLES

SELECT * FROM #[Dataset]

##There are manual ways to do this through code.
##Not relevent in todays age
##If you started out with text file we'll convert to csv before importing

##Joining/Appending Tables

CREATE TABLE tblCountry (
CountryID INT NOT NULL PRIMARY KEY,
CountryName VARCHAR(30) NOT NULL);

INSERT INTO tblCountry VALUES
(1,"India"),
(2,"Nepal")


CREATE TABLE tblState (
StateID INT NOT NULL PRIMARY KEY,
CountryID INT  ,
StateName VARCHAR(30) NOT NULL);

INSERT INTO tblState VALUES 
(1,1,"Maharastra"),
(2,1 ,"Punjab"),
(3,2,"Kathmandu"),
(4,NULL,"California")

SELECT * FROM tblCountry
SELECT * FROM tblState

###Inner Join (Appending) [Main Application]
###Joining columns from a table onto a different table using a specific column (usually a key)


SELECT * FROM tblCountry
		INNER JOIN tblState
        ON tblCountry.CountryID=tblState.CountryID
        
###Left Join 
###Joining the tables in terms of the table being joined

SELECT * FROM tblCountry
		LEFT JOIN tblState
        ON tblCountry.CountryID=tblState.CountryID
        
###Right Join 
###Joining the tables in terms of the table trying to join


SELECT * FROM tblCountry
		RIGHT JOIN tblState
        ON tblCountry.CountryID=tblState.CountryID
        
###Full Outer Join
###Joining in terms of both tables

SELECT * FROM tblCountry
LEFT JOIN tblState ON tblCountry.CountryID = tblState.StateID
UNION
SELECT * FROM tblCountry
RIGHT JOIN tblState ON tblCountry.CountryID= tblState.StateID
        
##Enriching Aggegate Measures

CREATE TABLE Table4 (
ID INT  NOT NULL,
Value1 INT NOT NULL,
Value2 INT NOT NULL);

INSERT INTO Table4 VALUES
(1, 1, 2),
(1, 2, 2),
(2, 3, 4),
(2, 4, 5)

SELECT * FROM Table4 

##Sum Values by ID
SELECT  ID, SUM(VALUE1), SUM(VALUE2)
FROM    tableName
GROUP   BY ID

##Add columns of Value1 and Value2
SELECT  ID, VALUE1 + VALUE2
FROM    TableName


##Now group by a ID
SELECT  ID, SUM(VALUE1 + VALUE2)
FROM    tableName
GROUP   BY ID

###Same could be done with division (/), multiplication (*), and subtraction (-)
###Many different functions you could use (list was in the video).










