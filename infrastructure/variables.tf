#criação de nova variáveis para a Aula 4.2 Terraform - Uso básico

variable "base_bucket_name" {
  default = "datalake-igti-tf"
}

variable "ambiente" {
  default = "producao"
}

variable "aws_account_id" {
  default = "530623260384"
}

variable "aws_region" {
  default = "us-east-1"
}


#criação de nova variável para o Use case 1 - Lakehouse com DeltaLake e EMR

variable "lambda_function_name" {
  default = "IGTIexecutaEMR"
}