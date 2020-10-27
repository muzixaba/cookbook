-- Create a database
-- CREATE DATABASE database_name;
-- USE database_name; --Needed for MySQL to switch into the db

-- Create a tables inside a database
-- CREATE TABLE author (
--     author_id INTEGER NOT NULL PRIMARY KEY,
--     first_name VARCHAR,
--     last_name VARCHAR
-- );

-- CREATE TABLE book (
--     book_id INTEGER NOT NULL PRIMARY KEY,
--     author_id INTEGER REFERENCES author,
--     title VARCHAR
-- );

/*
-- joining table (many-to-many)
CREATE TABLE author_publisher (
    author_id INTEGER REFERENCES author,
    publisher_id INTEGER REFERENCES publisher
);
*/

-- Insert Single Record


-- Insert Multiple Records


-- Read metadata
/* gets table structure on sqlite
PRAGMA table_info(flights);
*/

-- Search for records using sing table
/*
SELECT column_name(s)
FROM table_name
WHERE <condition> AND <condition>
GROUP BY column_name
ORDER BY column_name DESC
LIMIT #;
*/

-- Count number of unique entries in a specific column
/*
select count(distinct col_name) from table_name;
*/

-- Get max value in certain column
/*
select max(col_name) from table_name;
*/

-- Search for records using multiple tables


-- Search using wildcards ('%', '_')


-- Update single record
/*
UPDATE table_name 
   SET column1 = value1;

UPDATE author
SET first_name = 'Richard', last_name = 'Bachman'
WHERE first_name = 'Stephen' AND last_name = 'King';

*/

-- Update multiple records
/*
UPDATE table_name 
SET column1 = value1, column2 = value2,
WHERE <condition>;
*/


-- Delete single record
/*
DELETE FROM author
WHERE first_name = 'Paul'
AND last_name = 'Mendez';


*/

-- Delete mutlipe records


-- Delete all records in a table
/*
DELETE FROM table_name
WHERE <condition>;
*/

-- Delete an entire table
/*
DROP TABLE table_name;
*/


-- Joining Tables
-- Join Types (Inner, Full, Left, Outer, Cross)
/*
SELECT column(s)
FROM table1
<join_type> JOIN table2
ON <Join condition>
*/

-- Grouping Results (groupby)
/*
SELECT column_name(s)
FROM table_name
GROUP BY column_name
HAVING <boolean_condition>;
*/


-- Calculated Fields
/*
SELECT count(col)
FROM table_name;
*/