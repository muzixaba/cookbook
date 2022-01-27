from pyspark.sql import SparkSession
from pyspark.sql import Row

spark = (SparkSession
        .builder
        .getOrCreate())

schema = "Township STRING, Province STRING"
rows = [Row("Umlazi", "KZN"), Row("Soweto", "GP"), Row("Nyanga", "CPT")]
townships_df = spark.createDataFrame(rows, schema)

townships_df.show()