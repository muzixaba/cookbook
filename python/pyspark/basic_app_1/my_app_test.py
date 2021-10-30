import unittest
from datetime import date
from my_app import to_date_df
from pyspark.sql import SparkSession, Row
from pyspark.sql.types import StringType, StructType, StructField, DateType
from pyspark.sql import functions as F

def to_date_df(df, fmt, fld):
    return df.withColumn(fld, F.to_date(F.to_date(fld, fmt)))

class RowDemoTestCast(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.spark = SparkSession.builder \
            .master("local[3]") \
            .appName("RowDemoTest") \
            .getOrCreate()


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


        my_rdd = cls.spark.sparkContext.parallelize(my_rows, 2)
        cls.df = cls.spark.createDataFrame(my_rdd, my_schema)


    def test_date_type(self):
        """
        Check if row entries in EventDate are dates
        """
        rows = to_date_df(self.df, "M/d/y", "EventDate").collect()
        for row in rows:
            self.assertIsInstance(row["EventDate"], date)


    def test_data_value(self):
        """
        Check if row entries in EventDate are dates
        """
        rows = to_date_df(self.df, "M/d/y", "EventDate").collect()
        for row in rows:
            self.assertEqual(row["EventDate"], date(2020, 3, 5))


if __name__ == "__main__":
    unittest.main()