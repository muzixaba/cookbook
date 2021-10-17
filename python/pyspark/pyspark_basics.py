import pyspark
from pyspark.sql import SparkSession

# create a session
spark = SparkSession.builder.appName('SessionName').getOrCreate()
print(spark) # print session details

# create datafame from csv
df = spark.read.csv('some_file.csv')

# create datafame from csv with headers & infer data types
df_2 = spark.read.csv('some_file.csv', header=True, inferSchema=True)

# show/view dataframe
df.show()

# print dataframe schema
df.printSchema()

# get column names
df.columns

# get top 5 entries
df.head()

# get single column
df.select('ColName')

# get multiple columns
df.select(['col_1', 'col_2'])

# check data types inside dataframe
df.dtypes

# describe dataframe
df.describe().show()

# create new column from existing one
df.withColumn('NewColumnName', df['ExistingColumn']+5)

# drop a column
df.drop('ColName')

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

# rename column
df.withColumnRenamed('OldName', 'NewName')

# filter operations ????
df.filter(df['ColName']<=3000)

# mutliple filters (and==&, or==|)
df.filter((df['Col1']<=3000) & (df['col2']>200))

# using inverse condition
df.filter(~df['Age']>18) # not older than 18

# groupby
df.groupby('Col1').sum() #mean(), count(), agg()

