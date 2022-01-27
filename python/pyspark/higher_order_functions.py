# What are higher order functions?
# Functions that take in other function(s) are arguments

#%%
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.types import *
# %%
schema = StructType([StructField("celsius", ArrayType(IntegerType()))])
# %%
spark = (SparkSession
        .builder
        .appName("HigherOrderFunctions")
        .getOrCreate())


#%%
t_list = [[35, 36, 32, 30, 40, 42, 38]], [[31, 32, 34, 55, 56]]
t_c = spark.createDataFrame(t_list, schema)
# create temp view from df
t_c.createOrReplaceTempView("tC")
# %%
t_c.show(truncate=False) 
# %%
# Use TRANSFORM to apply a function to all elements in input array
(spark.sql(
    """
    SELECT celsius, transform(celsius, t -> ((t*9) div 5) + 32) as fahrenheit
    FROM tC
    """)).show()
# %%
# Use FILTER to produce an array of elembents that meet a certain condition
# show temperatures above 38 degress celsius
(spark.sql(
    """
    SELECT celsius, filter(celsius, t -> (t > 38)) as high
    FROM tC
    """)).show()

# %%
# Use EXISTS to check if any element returns True for a given condition
(spark.sql(
    """
    SELECT celsius, exists(celsius, t -> (t = 38)) as threshold
    FROM tC
    """)).show()
# %%
# Use Reduce to reduce the elements in an array to a single value
# reduce(expr, start, merge [, finish] )

(spark.sql(
    """
    SELECT celsius,
            reduce(
                celsius,
                0,
                (t, acc) -> t + acc,
                acc -> (acc div size(celsius) * 9 div 5) + 32
            ) as avgFahrenheit
    FROM tC
    """)).show()
# %%
spark.stop()
# %%
