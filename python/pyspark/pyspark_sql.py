from pyspark.sql import functions as F
from pyspark.sql import SparkSession, SparkContext

# create context & session
sc = SparkContext.getOrCreate()
spark = SparkSession(sc)

# run sql inside a df using F.expr()
df.select(F.col('col1'), F.col('col2'),
     F.expr("col2 + 5 as new_col")
  ).show()

# create a view
df.createOrReplaceTempView("table_name")


# simple select statement
spark.sql("""SELECT * from table_name""")


# CASE
spark.sql("""
        SELECT col1, col2,
        CASE
        WHEN col_name > 1 THEN 'buy'
        WHEN col_name < 2 THEN 'sell',
        ELSE 'wait'
        END AS 'buy_sell_guide'
        FROM table_name
        """)


# create spark database
spark.sql("CREATE DATABASE IF NOT EXISTS db_name")
spark.sql("USE db_name")

# create a managed table
df.write.saveAsTable('table_name')

# list databases
spark.catalog.listDatabases()

# list all tables
spark.catalog.listTables()

# list columns in specific table
spark.catalog.listColumns('table_name')

# describe a specific table
spark.sql("DESCRIBE FORMATTED db_name.table_name").show()

# create a view
df.createOrReplaceTempView('table_name')

# select everything inside table
spark.sql("""SELECT * FROM table_name""")

# view additional meta data
spark.sql("SHOW TBLPROPERTIES db_name.table_name").show()

# set table properties
properties = {'description': 'Table used to buy/sell bitcoin', 
              'created_by': 'John Doe'}
spark.sql(f'ALTER TABLE bitcoin.bitcoin_advice SET TBLPROPERTIES (PROPERTIES = "{properties}")')


# case statement
spark.sql("""
        SELECT col1, col2, col3
        CASE
        WHEN col3 < 1 THEN 'less than 1'
        WHEN col3 > 1 THEN 'greater than 1'
        ELSE 'equal to 1'
        END AS valueComparedTo1
        FROM table_name
        ORDER BY datetime_col DESC
        """)


# groupby
spark.sql("""
        SELECT col1, col2, COUNT(col3)
        FROM table_name
        WHERE time_col > '2020-01-02'
        GROUP BY col3
        """)

# return table as dataframe
spark.table('table_name')

# check table properties
spark.sql('DESCRITBE FORMATTED db_name.table_name')

#-------
# NOTES
#-------

# can only run sql on a table or a view using `spark.sql`

# can run sql queries on both structured and semi-structured data (json)

# view database(s) and table(s)
# spark.catalog.listDatabases()
# - default db used by default
# spark.catalog.listTables()
# spark.catalog.listColumns()


# all custom code passes through 'Spark SQL Engine' hence sql imports.
# SQL Engine does the following:
# - Analyses your code
# - Optimises it
# - Creates execution plan
# - Generates final code

# as performant as the df api
# Table meta data stored in hive metastore (/user/hive/warehouse)
# Managed Table - Data & Meta data managed by spark
# Unmanaged Table - Spark only manages the meta data

# DROP TABLE table_name
# - Drops both the table & metadata if managed table
# - Only terminates metadata in unmanaged table

# You can mix DataFrame & SQL API code