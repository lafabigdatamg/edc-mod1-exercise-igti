import threading
import os
import sys
import boto3


# criando thread para validação do processo de uplaoad
class ProgressPercentage(object):

    def __init__(self, filename):
        self._filename = filename
        self._size = float(os.path.getsize(filename))
        self._seen_so_far = 0
        self._lock = threading.Lock()

    def __call__(self, bytes_amount):
        # To simplify, assume this is hooked up to a single filename
        with self._lock:
            self._seen_so_far += bytes_amount
            percentage = (self._seen_so_far / self._size) * 100
            sys.stdout.write(
                "\r%s  %s / %s  (%.2f%%)" % (
                    self._filename, self._seen_so_far, self._size,
                    percentage))
            sys.stdout.flush()


# Criar um cliente para interagir com o AWS S3
s3_client = boto3.client('s3')

s3_client.upload_file('data/MICRODADOS_ENEM_2020.csv',
                      'datalake-eric-530623260384',
                      'raw-data/MICRODADOS_ENEM_2020.csv',
                      Callback=ProgressPercentage('data/MICRODADOS_ENEM_2020.csv'))
