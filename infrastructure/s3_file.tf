resource "aws_s3_object" "codigo_spark" {
  bucket = aws_s3_bucket.datalake.id
  key    = "emr-code/pyspark/job_spark_from_tf.py"
  acl    = "private"
  source = "../emr_job_spark_2020.py"
  etag   = filemd5("../emr_job_spark_2020.py")

}
