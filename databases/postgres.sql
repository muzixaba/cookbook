-- Check db server options
service postgresql

-- Start postgresql service
sudo service postgresql start

-- Get help
psql --help

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

-- Create db
createdb <db_name>

-- Drop db
dropdb <db_name>