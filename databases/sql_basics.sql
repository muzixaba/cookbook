-- Create a database


-- Create a table inside a database


-- Insert Single Record


-- Insert Multiple Records


-- Search for records using sing table
/*
SELECT column_name(s)
FROM table_name
WHERE <condition> AND <condition>
GROUP BY column_name
ORDER BY column_name DESC
LIMIT #;
*/

-- Search for records using multiple tables


-- Search using wildcards ('%', '_')


-- Update single record
/*
UPDATE table_name 
   SET column1 = value1;
*/

-- Update multiple records
/*
UPDATE table_name 
SET column1 = value1, column2 = value2,
WHERE <condition>;
*/


-- Delete single record


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