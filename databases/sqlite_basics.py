# import sqlite3
import sqlite3

# db connection string
sqlite:///relative/path.db
sqlite:////absolute/path/to.db
 

# create a database
conn = sqlite3.connect('example.db')
conn_mem = sqlite3.connect(":memory:") #in memory db

# create a cursor
cur = conn.cursor()

# Data types
# NULL (None)
# INTEGER (Int)
# REAL (Float)
# TEXT (Str)
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

def show_all(table: str):
    conn = sqlite3.connect('db_name.db')
    c = conn.cursor()
    c.execute(f"SELECT rowid, * FROM {table}")
    items = c.fetchall()
    for i in items:
        print(item)
    conn.commit()
    conn.close()

def find_one(email: str):
    conn = sqlite3.connect('db_name.db')
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM table_name WHERE email = (?)", (email,))
    items = c.fetchall()
    for i in items:
        print(i)
    conn.commit()
    conn.close()

def add_one(name: str, surname: str, email: str):
    conn = sqlite3.connect('db_name.db')
    c = conn.cursor()
    c.execute("INSERT INTO table_name VALUES (?,?,?)", name, surname, email)
    conn.commit()
    conn.close()

def add_many(lst):
    """Takes list of tuples"""
    conn = sqlite3.connect('db_name.db')
    c = conn.cursor()
    c.execute("INSERT INTO table_name VALUES (?,?,?)", (lst))
    conn.commit()
    conn.close()

def delete_one(id: str):
    conn = sqlite3.connect('db_name.db')
    c = conn.cursor()
    c.execute("DELETE FROM table_name WHERE rowid=(?)", id)
    conn.commit()
    conn.close()

# open sqlite db using cli tool
sqlite3 db_name.sqlite3

# get tables
.tables

# exit sqlite3 cli
.exit