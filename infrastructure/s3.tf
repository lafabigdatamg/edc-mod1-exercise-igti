
resource "aws_s3_bucket" "datalake" {
  # parâmetros de configuração do recurso escolhido
  bucket = "datalake-eric-igti-edc-tf"
  #bucket = "${var.base_bucket_name}-${var.ambiente}-${var.aws_account_id}"

  tags = {
    IES   = "IGTI",
    CURSO = "EDC"
  }
}

resource "aws_s3_bucket_acl" "datalake" {
  bucket = aws_s3_bucket.datalake.id
  acl    = "private"
}

resource "aws_s3_bucket_server_side_encryption_configuration" "datalake" {
  bucket = aws_s3_bucket.datalake.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}
resource "aws_s3_object" "codigo_spark" {
  bucket = aws_s3_bucket.datalake.id
  key    = "emr-code/pyspark/job_spark_from_tf.py"
  acl    = "private"
  source = "../emr_job_spark_2020.py"
  etag   = filemd5("../emr_job_spark_2020.py")

}
