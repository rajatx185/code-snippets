import boto3
import botocore


def download_file():
    BUCKET_NAME = 'mytestbucket'
    KEY = 'fileinbucket.txt'
    s3 = boto3.resource('s3')
    try:
        s3.Bucket(BUCKET_NAME).download_file(KEY, 'downloadname.txt')
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            raise