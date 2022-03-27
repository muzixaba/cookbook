# import sqlite3
import sqlite3

#Connection string
sqlite:///relative/path.db
sqlite:////absolute/path/to.db
 

# create a database
conn = sqlite3.connect('example.db')
conn_mem = sqlite3.connect(":memory:") --in memory db

# create a cursor
cur = conn.cursor()

# Data types
# NULL
# INTEGER
# REAL
# TEXT
# BLOB

# Create table
cur.execute('''CREATE TABLE stocks (
            date text, 
            trans text, 
            symbol text, 
            qty integer, 
            price real
            )''')

# Insert a row of data
cur.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Insert multiple records. Use list of tuples
customers = [
    ('Name', 'Surname', 'Email'),
    ('Name2', 'Surname2', 'Email2'),
    ('Name3', 'Surname3', 'Email3'),
    ] 
cur.executemany("INSERT INTO table_name VALUES (?,?,?)", customers)

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()

# Query the database
# rowid == Primary Key
cur.execute("SELECT rowid, * FROM table_name")
cur.fetchone() # returns a single result as a tuple
cur.fetchmany(3) # top 3 results
cur.fetchall() # fetches all

items = cur.fetchall()
for item in items:
    print(item)

# open sqlite db using cli tool
sqlite3 db_name.sqlite3

# get tables
.tables

# exit sqlite3 cli
.exit