/*
CREATE a database
*/

CREATE DATABASE mentorship;

/*
DROP a database
*/

DROP DATABASE mentorship;

/*
CREATE a table in the database
*/

USE mentorship

CREATE TABLE Persons (
    PersonID int,
    LastName varchar(255),
    FirstName varchar(255),
    Address varchar(255),
    City varchar(255)
);

/*
TEST if table has been created
*/
SELECT * FROM Persons;

/*
DROP a table in the database
*/

USE mentorship

DROP TABLE Persons;
/*
TRUNCATE a table in the database (remove data but not the table)
*/

USE mentorship

TRUNCATE TABLE Persons;

/*
ALTER TABLE (add and remove columns, rename columns change datatypes)
*/
USE mentorship

ALTER TABLE Persons
ADD Email varchar(255);

USE mentorship

ALTER TABLE Persons
DROP COLUMN Address;

USE mentorship

EXEC sp_rename 'Persons.LastName', 'Name', 'COLUMN';

/*
INSERT INTO add data to the table
*/

USE mentorship

INSERT INTO Persons(PersonID, Name, FirstName, City, Email)
VALUES ('1', 'Walbeek','Thabor','Pune','thabor@dathabor.com');

