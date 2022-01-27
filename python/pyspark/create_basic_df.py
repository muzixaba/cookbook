#%%
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

#%%
# create session
spark = (SparkSession
        .builder
        .appName("AuthorAges")
        .getOrCreate())

#%%
# create df
data_df = spark.createDataFrame(
    [("Muzi", 34), ("Nkanyezi", 4), ("Phumla", 25), ("Muzi", 20)],
    ["name", "age"])

#%%
# group by name, aggregate age
avg_df = data_df.groupBy("name").agg(F.avg("age"))


#%%
avg_df.show()

#%%
# stop session
spark.stop()
# %%
