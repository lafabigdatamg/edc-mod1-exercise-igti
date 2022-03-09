import boto3
import pandas as pd

# Criar um cliente para interagir com o AWS S3
s3_client = boto3.client('s3')

# Realizar upload de arquivos locais para bucket S3
s3_client.download_file("datalake-eric-igti-edc",
                        "data/ITENS_PROVA_2020.csv",
                        "data/ITENS_PROVA_2020.csv")

df = pd.read_csv("data/ITENS_PROVA_2020.csv", sep=";")
print(df)

# Realizar download de arquivos do bucket S3 para máquina local
s3_client.upload_file("data/ITENS_PROVA_2019.csv",
                      "datalake-eric-igti-edc",
                      "data/ITENS_PROVA_2019.csv")
