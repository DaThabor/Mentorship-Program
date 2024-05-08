/*
Select all rows and columns
*/
SELECT * FROM Application.Countries;

/*
Select Top 10
*/
SELECT TOP 10 * FROM Application.Countries;

/*
Select Unique Values from a Column
*/
SELECT DISTINCT CountryName FROM Application.Countries;

/*
Select Distinct from Orders Table
*/
SELECT DISTINCT SalespersonPersonID FROM Sales.Orders;

/*
But if added with the ID values it will look like
*/
SELECT DISTINCT OrderID, SalespersonPersonID FROM Sales.Orders;

/*
Get the count of distinct Country Names
*/
SELECT COUNT(DISTINCT CountryName) FROM Application.Countries;

/*
Get the count of distinct Country Names without the DISTINCT function
*/
SELECT COUNT(CountryName) FROM Application.Countries;

/*
And renaming the column name for COUNT
*/
SELECT COUNT(CountryName) as Count FROM Application.Countries;

/*
Using the WHERE clause with text
*/
SELECT CountryName FROM Application.Countries
WHERE CountryName = 'Albania';

/*
Using the WHERE clause with number
*/
SELECT CountryName FROM Application.Countries
WHERE CountryID = 3;

/*
Using the WHERE clause with operators
*/
SELECT CountryName FROM Application.Countries
WHERE CountryID > 100;

/*
Check the initial dataset
*/
SELECT Region, CountryName FROM Application.Countries;

/*
Using the ORDER BY clause
*/
SELECT Region, CountryName FROM Application.Countries
ORDER BY Region;

/*
Using the ORDER BY clause with DESC and ASC
*/
SELECT Region, CountryName FROM Application.Countries
ORDER BY Region ASC, CountryName DESC;

/*
Using AND operator (all conditions must be TRUE)
*/
SELECT Region, CountryName FROM Application.Countries
WHERE Region = 'Asia' AND CountryName LIKE 'I%';

/*
Using AND  and OR operator
*/
SELECT Region, CountryName FROM Application.Countries
WHERE Region = 'Asia' AND (CountryName LIKE 'I%' OR CountryName LIKE 'J%');

/*
Using OR operator
*/
SELECT Region, CountryName FROM Application.Countries
WHERE CountryName LIKE 'I%' OR CountryName LIKE 'K%';

/*
Using NOT operator
*/
SELECT Region, CountryName FROM Application.Countries
WHERE NOT CountryName LIKE 'I%';

/*
Using NOT BETWEEN operator
*/
SELECT CountryID, Region, CountryName FROM Application.Countries
WHERE CountryID NOT BETWEEN 1 and 3;

/*
Using NOT IN operator
*/
SELECT Region, CountryName FROM Application.Countries
WHERE CountryName NOT IN ('Algeria', 'Angola');

/*
Using NOT Greater Than operator
*/
SELECT CountryID, Region, CountryName FROM Application.Countries
WHERE NOT CountryID >100;

/*
Using NOT Less Than operator
*/
SELECT CountryID, Region, CountryName FROM Application.Countries
WHERE NOT CountryID <100;
