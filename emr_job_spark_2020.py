#comentário para modificar o arquivo py
from pyspark.sql.functions import mean, max, min, col, count
from pyspark.sql import SparkSession

spark = (
    SparkSession.builder.appName("ExerciseSpark")
    .getOrCreate()
)

#Ler os dados do enem 2020
enem = (
    spark
    .read
    .format("csv")
    .option("header", True)
    .option("inferSchema", True)
    .option("delimiter", ";")
    .load("s3://datalake-eric-530623260384/raw-data/")
)

(
    enem
    .write
    .mode("overwrite")
    .format("parquet")
    .save("s3://datalake-eric-530623260384/consumer-zone/")
)