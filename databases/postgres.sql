-- Check db server options
service postgresql

-- Start postgresql service
sudo service postgresql start

-- Get help
psql --help
\?

-- Login to postgresql using default user
sudo su postgres

-- Launch postgres command line tool
psql

-- List databases
\l

-- List users
\du

-- Connect to specific db using logged  in user
\c <db_name>

-- Change user password
ALTER USER <user_name> WITH PASSWORD 'password';

-- Create new user
CREATE USER <user_name> WITH PASSWORD 'password';

-- Provide privileges to user
ALTER USER <user_name> WITH <PRIVILEGE>;

-- Delete user
DROP USER <user_name>;

-- View man page for psql
man psql

-- Connect to specific db using a certain user
psql -d <db_name> -U user <user_name> -W

-- List tables in current db
\dt

-- Describe a table
\d <table_name>

-- Edit command in external editor
\e

-- Quit psql
\q

-- Toggle expanded display
\x

-- List available functions
\df

-- Execute commands from a file
\i path/to/file.sql

-- Create db
--createdb <db_name> ???
CREATE DATABASE <db_name>;

-- Drop db
--dropdb <db_name> ???
DROP DATABASE <db_name>;

-- Drop a table
DROP TABLE <table_name>;


-- Create a Table (without constrainsts)
CREATE TABLE person (
    id INT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    gender VARCHAR(7),
    date_of_birth DATE
);

-- Create a Table (with constrainsts)
CREATE TABLE person (
    id BIGSERIAL NOT NULL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    gender VARCHAR(7) NOT NULL,
    date_of_birth DATE NOT NULL,
    email VARCHAR(150)
);

-- Insert record into table
INSERT INTO person (
    first_name,
    last_name,
    gender,
    date_of_birth
)
VALUES ('Muzi', 'Xaba', 'Male', DATE '1987-08-24');


-- Add constraint to existing column
ALTER TABLE person ADD CONSTRAINT gender_constraint CHECK (gender='Female' OR gender='Male');



/*
CREATING TABLES WITH RELATIONSHIPS
*/
CREATE TABLE car (
    id BIGSERIAL NOT NULL PRIMARY KEY,
    make VARCHAR(100) NOT NULL,
    model VARCHAR(100) NOT NULL,
    price NUMERIC(19, 2) NOT NULL
);

CREATE TABLE person (
    id BIGSERIAL NOT NULL PRIMARY KEY,
    first_name  VARCHAR(50) NOT NULL,
    las_name  VARCHAR(50) NOT NULL,
    gender VARCHAR(7) NOT NULL,
    email VARCHAR(150),
    date_of_birth DATE NOT NULL,
    country_of_birth VARCHAR(50) NOT NULL,
    car_id BIGINT REFERENCES car(id),
    UNIQUE(car_id)
);



insert into person (first_name, last_name, gender, email, date_of_birth, country_of_birth)
values ("Muz", "Xab", "Male", '1977-05-23', 'South Africa');

insert into person (first_name, last_name, gender, email, date_of_birth, country_of_birth)
values ("Nkanyi", "Xab", "Female", '2017-04-23', 'South Africa');

insert into person (first_name, last_name, gender, email, date_of_birth, country_of_birth)
values ("Phumla", "Ntenz", "Femal", '1999-07-23', 'South Africa');


insert into car (make, model, price) values ("BMW", "M3", 600000);
insert into car (make, model, price) values ("Hyundai", "Atos", 100000);


-- Update Foreign Key records
UPDATE person SET car_id = 2 WHERE id = 1;

-- Export query results to CSV (include headers)
\copy (<sql_query_excl_;>) TO '/path/to/file.csv' DELIMITER ',' CSV HEADER;

-- Restart a sequence
ALTER SEQUENCE <sequence_name> RESTART WITH <start_number>;

-- Add extension to postgres server
CREATE EXTENSION IF NOT EXISTS 'ext_name';