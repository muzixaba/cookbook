#%%
from pyspark.sql import functions as F
from pyspark.sql import SparkSession

#%%
# Start spark session
spark = SparkSession.builder \
        .master("local[3]") \
        .appName("LogFileDemo") \
        .getOrCreate()

#%%
# READ in data
file_df = spark.read.text("data/apache_logs.txt")
file_df.printSchema()
# %%
# use regex to select fields in string
log_reg = r'^(\S+) (\S+) (\S+) \[([\w:/]+\s[+\-]\d{4})\] "(\S+) (\S+) (\S+)" (\d{3}) (\S+) "(\S+)" "([^"]*)'
# regexp_extract(str, pattern, idx)
logs_df = file_df.select(
    F.regexp_extract('value', log_reg, 1).alias('ip'),
    F.regexp_extract('value', log_reg, 4).alias('date'),
    F.regexp_extract('value', log_reg, 6).alias('request'),
    F.regexp_extract('value', log_reg, 10).alias('referrer'),
)
logs_df.printSchema()
# %%
logs_df \
    .withColumn("referrer", F.substring_index("referrer", "/", 3)) \
    .groupBy("referrer") \
    .count() \
    .show(100, truncate=False)
# %%

# %%
