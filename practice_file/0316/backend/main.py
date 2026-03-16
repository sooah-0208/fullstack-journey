# python으로 spark 실행하기

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("PySpark WorkCount Test").master("spark://localhost:7077").getOrCreate()
