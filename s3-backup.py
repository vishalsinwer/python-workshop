import boto3

s3 = boto3.resource("s3")
def show_bucket(s3):
     for bucket in s3.buckets.all():
          print(bucket.name)
def create_buckets(s3):
     s3.create_bucket(Bucket="my-buck-000000",
                      CreateBucketConfiguration={
                      'LocationConstraint': 'ap-south-1',
                      },)
     print("bucket created success")
create_buckets(s3)  
show_bucket(s3)   
 
          