import pyspark
from pyspark.sql import SparkSession

# create a session
spark = SparkSession.builder.appName('SessionName').getOrCreate()
print(spark) # print session details

# create a session with Hive Metastore support
spark = SparkSession \
            .builder \
            .appName('SessionName') \
            .enableHiveSupport() \
            .getOrCreate()

# create datafame from csv
df = spark.read.csv('some_file.csv')

# create datafame from csv with headers & infer data types
df_2 = spark.read.csv('some_file.csv', header=True, inferSchema=True)

# show/view dataframe
# good for debbuging
df.show()

# show specific number of rows
df.show(10)

# print dataframe schema
df.printSchema()

# get column names
df.columns

# show data types
df.dtypes

# get top 5 entries
df.head()

# change all column names
df.toDF('col1', 'col2', 'col3')

# get single column
df.select('ColName')

# get multiple columns
df.select(['col_1', 'col_2'])

# check data types inside dataframe
df.dtypes

# summary statistics, describe dataframe
df.describe().show()

# repartition a df into 2 parts
df.repartition(2)

# create new column from existing one
df.withColumn('NewColumnName', df['ExistingColumn']+5)

# drop a column
df.drop('ColName')

# drop multiple columns
df.drop("col1", "col2")

# drop duplicates using one or more columns
df.drop_duplicates(['col1', 'col2'])

# drop rows with null values (if any value is null)
df.na.drop()

# drop rows with null values, using threshold of 3
df.na.drop(how='any', thresh=3)

# drop rows with null values from a specific column
df.na.drop(how='any', subset=['ColName'])

# fill all missing values with sing value
df.na.fill('NewValue')

# fill missing values from specific column
df.na.fill('new_value', 'ColName')

# fill missing values from multiple columns
df.na.fill('new_value', ['col1', 'col2'])

# impute null value using mean
from pyspark.ml.feature import Imputer
imputer = Imputer(
    inputCols=['col1', 'col2'],
    outputCol=["{}_imputed".format(x) for x in ['col1', 'col2']],
    ).setStrategy("mean") # median
imputer.fit(df).transform(df)

# rename individual/list of columns
df.withColumnRenamed('OldName', 'NewName')

# filter operations ????
df.filter(df['ColName']<=3000)

# mutliple filters (and==&, or==|)
df.filter((df['Col1']<=3000) & (df['col2']>200))

# using inverse condition
df.filter(~df['Age']>18) # not older than 18

# groupby
df.groupby('Col1', 'Col2').sum() #mean(), count(), agg()

# groupby with mutliple agg functions for different columns
df.groupBy(F.year('Col')) \
  .agg({'Col2': 'max', 'Col3': 'sum'})

# use alias to name groupby columns
df.dropna().groupBy(F.year('timestamp'))\
    .agg({'high': 'max', 'volume_currency': 'sum'})\
    .select(F.col('year(timestamp)').alias('year_agg'), 
            F.col('max(high)').alias('max'), 
            F.col('sum(volume_currency)').alias('volume_sum'))\
    .orderBy('year(timestamp)').show(10, False)
    
# collect df as list of rows
df.collect()

# order by certain column
df.orderBy('col')

# apply a function to the 2nd column of dataframe
df.map(lambda x: x[1] * 2)

# create a new df from an existing one
df.select(['col1', 'col2'])

# define the schema of a dataframe & create df from it
schema = StructType([StructField('id', IntegerType()),
                    StructField('name', StringType()),
                    StructField('count', IntegerType())])
df = spark.createDataFrame(data, schema=schema)

# get dataframe schema
df.printSchema()

# fill nulls/na
df.fillna()

# fill nulls/na of specific columns
df.fillna({"col1": "newValue", "col2": "newValue"})

# drop rows with nulls/na
df.na.drop()

# drop columns with nulls/na
df.na.drop(subset='colName')

# replace values in df
df.replace("OldValue", "NewValue")

# drop a df column
df.drop("colName")

# sort df using a specific column, in descending order
df.sort(expr("ColName desc"))

# change column type for spark functions
from pyspark.sql import functions as F
df.withColumn(colName='Timestamp', col=F.to_timestamp(df['Timestamp']))

# using row conditional statements
df.withColumn('condition', \
  F.when(df.col1>20, 1) \
    .when(df.col2==4, 2) \
    .otherwise(3))

# add new column or replace existing
# df.withColumn("ColName", colomn_expression)
df = df.withColumn('NewCol', F.year(F.col('Timestamp')))

# filter dataframe using where
df.where(F.col('Timestamp') > datetime.date(2021, 1, 1))

# pick a subset of the dataframe
# Takes in column object(s) and or string
df.select(column('col1'), col('col2'), df.col3, "col4")

# change an expression to column object
df.select("col1", F.expr("F.to_date(concat(YearCol,MonthCol,DayofMonthCol),'yyyyMMdd') as NewDate"))

# save dataframe as parquet (recommended file format)
df.write.format("parquet").save("path/to/data")

# use sql on a spark session
spark.sql()

# create an RDD with 2 partitions
spark.sparkContext.parallelize(data, 2)

# create DataFrame from RDD
df4rmRDD = spark.createDataFrame(my_rdd, my_schema)

# Change column data types by casting
df4 = df2.withColumn("Col1", col("Col1").cast(IntegerType())) \
        .wichColumn("Col2", col("Col2").cast(StringType()))

# get number of partitions of a df
df.rdd.getNumPartitions()

# get number of records in each partition
df.groupBy(F.spark_partition_id()).count().show()

# repartition a df
df.repartition(n)
df.partitionBy(col1,col2) # creates a tree of folders
df.bucketBy(n,col1,col2) # partion data by buckets if partition column as many unique values

# create a user defined function (must be deterministic)
from pyspark.sql.types import DoubleType, IntegerType, StringType
# F.udf(lambda, return_type)
fn = F.udf(lambda x : x*2, DoubleType())
# applying user defined function
df.withColumn('col2', fn(df.col1))

# add id column to df
df2 = df.withColumn("id", F.monotonically_increasing_id())

# use built-in function that's not part of functions
# get percentiles of a specific column
# uses sql expressions
df.selectExpr(
  "percentile_approx(col_name, (array(0.25, 0.5, 0.75)) as col_name"
).show()
# merge/join dataframes
left_df.join(righ_df, on='key')
left_df.join(righ_df, left_df.col1 == right_df.col_3)

# pivot table
df.groupBy('A', 'B').pivot('C').sum('D')

# create a temp view/table to use sql on
df.createOrReplaceTempView('bitcoin_tbl')

# Apply SwitchCase using when() on df
df4 = df.withColumn("Year", \
        when(col("year") < 21, col("year") + 2000)
        .when(col("year") < 100, col("year") + 1900) \
        .otherwise(col("year")))

# new column using sql CASE expression
# spark.sql() method returns a DataFrame
traffic_light = spark.sql("""SELECT timestamp, high, low, open,
            CASE
            WHEN colour = 'red' THEN 'Stop'
            WHEN colour = 'amber' THEN 'Caution'
            WHEN colour = 'green' THEN 'Go'
            ELSE 'Traffic lights not working'
            END AS traffic_light
            FROM traffic_tbl
            ORDER BY timestamp DESC""")


# groupby using sql
spark.sql("""SELECT traffic_light, COUNT(red)
          FROM traffic_tbl
          WHERE timestamp > '2020-01-02'
          GROUP BY traffic_light""")


# aggregate df using sql expressions
df.selectExpr(
    "count(*) as 'count 1'",
    "count(ColName) as 'count ColName",
    "sum(Col2) as TotalCol2"
)

# groupby using sql
spark.sql("""
    SELECT Col1, Col2, sum(Col3) as TotalCol3,
    FROM table_view_name
    GROUP BY Col4, Col5
""")

# create a spark database
spark.sql("CREATE DATABASE IF NOT EXISTS DATABASE_NAME")

# connect to specific spark database
spark.catalog.setCurrentDatabase("DATABASE_NAME")

# list tables inside spark database
spark.catalog.listTables("DATABASE_NAME")

# PySpark Logging (Log4J)
# Requirements
# - Log4J config file (log4j.properties)
# - Configure Spark JVM to pickup the Log4J config file
# - Create python class to get Log4J's instance

# config used to pass values to Spark driver JVM
spark.driver.extraJavaOptions

# tell spark that the log4j.properties file is present in the current directory
-Dlog4j.configuration=file:log4j.properties

# tell YARN log aggregator where to find the logs
# also tell the log file appender where to create logs
spark.yarn.app.container.log.dir

# define spark.driver.extraJavaOptions in this file
SPARK_HOME/conf/spark-defaults.conf

# logger.py
class Log4J:
    def __init__(self, spark):
        log4j = spark._jvm.org.apache.log4j
        root_class = "guru.learningjournal.spark.examples"
        conf = spark.sparkContext.getConf()
        app_name = conf.get("spark.app.name")
        self.logger = log4j.LogManager.getLogger(f"{root_class}.{app_name}")

    def warn(self, message):
        self.logger.warn(message)

    def info(self, message):
        self.logger.info(message)

    def error(self, message):
        self.logger.error(message)

    def debug(self, message):
        self.logger.debug(message)
    
# Stopping a spark application
spark_session_var.stop()

# USER DEFINES FUNCTIONS
# create function
def my_funct(x):
    return x + "updated"

# register the function as df udf, udf(function_name, return_type)
my_udf = udf(my_funct, StringType())

# apply df udf as column expression
df2 = df.withColumn("ColName", my_udf("ColName"))

# register udf as sql function
spark.udf.register("udf_name", my_funct, StringType())

# apply sql udf to a column
df3 = df.withColumn("ColName", expr("udf_name(ColName)"))

# PLOTS

# histogram
# grab a sample of the data, turn to pandas df, then plot
df.sample(False, 0.1).toPandas().hist()


#--------------------
# Spark vs Pandas
#------------------
# https://www.youtube.com/watch?v=XrpSRCwISdk 
# What's Spark? An engine for large scale data processing
# Spark works on distributed compute
# 2 main abstractions
#   RDD - Distributed collection of objects
#   Dataframe - Distributed dataset of tabular data

# Main Ideas
# Spark objects are immutable
# Does lazy evaluation

# Architecture
# User -> Driver -> Master [Executors] -> Data

# Machine Learning
# MLlib, the equivalent of scikit-learn

# What's RDD & It's Benefits (Unstructure API)
# - Low-level API
# - Immutable, distributed data structure 
# - Great with unstructured data (media/text/etc)
# - No need for schema/structure
# - Tell spark 'how' to do something
# - Fault tolerant
# - Need access to the spark context to use RDDs

# Structured APIs (DataFrames, Datasets, SQL)
# - High level APIs
# - Easy to use/read
# - You tell spark 'What to do' e.g mean, max, etc
# - Datasets = RDD + DataFrames

# SQL API
# Can only be used in a table or view
# Takes in spark.sql() method and returns a DataFrame

# The different ways to use spark
# Local Mode - CLI


# Spark Cluster Managers
# local[n] - Works on local machine 
#   local[1], has driver only
#   local[3], has driver and 2 executors

# YARN
# Mesos
# Kubernetes
# Standalone


# Spark Configurations

# specify configs (spark.conf)
[SPARK_APP_CONFIGS]
spark.app.name = AppName
spark.master = local[3] # cluster manager (will run 3 threads)

# Spark Execution/Deployment Modes
# Client Mode
# Cluster Mode



# PySpark CLI

# get help
pyspark --help

# run pyspark locally with 3 threads and give the driver 2G of memory
pyspark --master local[3] --driver-memory 2g

# Transformations (Lazy execution)
# - Narrow : Requires a single partition to produce valid results.
# - Wide : Requires data from multiple partitions to produce valid results. e.g. groupby, join

# Transformations
# Combining DataFrames
# Aggregations (simple, grouping, windowing)
#   Simple - Aggregate the entire df, return a single value(s), per column
# Applying built-in functions
# Applying User-Defined-Functions (UDF)
# Referencing Rows/Columns
# Creating column expressions

# Actions (Eager execution)
# Read
# Write
# Show
# Collect



#----------
# SPARK UI
#----------

# JOBS

# STAGES

# STORAGE

# ENVIRONMENT

# EXECUTORS

# SQL


#-----------------
# SPARK TABLES
#-----------------

# Managed Tables

# create a managed table (creates table metadata & saves table in spark sql warehouse)
df.write.saveAsTable('table_name')


# Unmanaged Tables (external)

# create an unmanaged table (creates table metadata & saves table in specified location)
CREATE TABLE table_name(col1 type, col2 type, ...) 
  USING PARQUET 
  LOCATION 'path/to/location'