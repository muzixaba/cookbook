#%%
import pyspark
from pyspark.sql import SparkSession, Row
from pyspark.sql.types import StringType, StructField, StructType
from pyspark.sql import functions as F

#%%
# if __name__ == "__main__":
# connect to spark session
spark = SparkSession \
            .builder \
            .master("local[3]") \
            .appName("RowDemo") \
            .getOrCreate()


# create data for DataFrame or import data
my_schema = StructType([
    StructField("ID", StringType()),
    StructField("EventDate", StringType())
])

my_rows = [
    Row("123", "03/05/2020"),
    Row("124", "3/5/2020"),
    Row("125", "03/5/2020"),
    Row("126", "3/05/2020")
]

#%%
# create rdd from rows
my_rdd = spark.sparkContext.parallelize(my_rows, 2)

#%%
# create df from rdd
df = spark.createDataFrame(my_rdd, my_schema)

# %%
df.printSchema()
# %%
df.show()
# %%
# change date column to date format
def to_date_df(df, fmt, fld):
    return F.to_date(df, F.to_date(fld, fmt))
    
df2 = df.withColumn("EventDate", F.to_date("EventDate", "M/d/y"))
# %%
df2.printSchema()
# %%
df2.show()
# %%
