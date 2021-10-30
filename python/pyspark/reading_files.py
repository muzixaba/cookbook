#%%
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, DateType, StringType, IntegerType
# from lib.logger import Log4j

if __name__ == "__main__":
    spark = SparkSession.builder \
        .master("local[3]") \
        .appName("ReadFiles") \
        .getOrCreate()

    # SCHEMA (Use Spark Data Types)
    # 2 ways to define spark schemas:
    # - Programmatically( StructType([StructField()]) )
    # - Using DDL String( """Col1 INT, Col2 STRING, Col3 DATE""")

    # CSV
    csv_df = spark.read \
        .format("csv") \
        .option("header", "true") \
        .option("dateFormat", "M/d/y") \
        .load("path/to/file.csv")

    # JSON
    json_df = spark.read \
        .format("json") \
        .option("dateFormat", "M/d/y") \
        .load("path/to/file.json")


    # PARQUET (schema info comes with file)
    p_df = spark.read \
        .format("parquet") \
        .load("path/to/file.parquet")






    # WRITE OUT

    # save() method
    df.write \
        .format("parquet") \
        .mode(saveMode) \
        .option("path", "path/to/folder/") \
        .save()
    # What if file already exists in defined location
    #saveMode = append, overwrite, errorIfExists, ignore