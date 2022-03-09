import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# A partir daqui, exatamente o mesmo codigo executado no EMR

#Ler os dados do enem 2020
enem = (
    spark
    .read
    .format("csv")
    .option("header",True)
    .option("inferSchema",True)
    .option("delimiter",";")
    .load("s3://datalake-eric-530623260384/raw-data/")
)

#Escrever no Datalake em parquet
(
    enem
    .write
    .mode("overwrite")
    .format("parquet")
    .save("s3://datalake-eric-530623260384/consumer-zone/")
)

job.commit()

