// Connection string
sqlite:///relative/path.db
sqlite:////absolute/path/to.db

import sqlite3
con = sqlite3.connect('example.db')


cur = con.cursor()

# Create table
cur.execute('''CREATE TABLE stocks
               (date text, trans text, symbol text, qty real, price real)''')

# Insert a row of data
cur.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Save (commit) the changes
con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()


-- open sqlite db using cli tool
sqlite3 db_name.sqlite3

-- get tables
.tables

-- exit sqlite3 cli
.exit