"""
Chapter 10: Deploying Models with DVC

Example of reading a file using dvc.api.open from Chapter 10.
"""
import dvc.api
import json
import boto3

url = dvc.api.get_url(
    path="results/train_metrics.json",
    repo="https://github.com/PacktPublishing/Open-Source-MLOps-with-DVC-and-CML.git",
    rev="chapter-09",
    remote="s3",
)

bucket = url.split("/")[2]
print(f"bucket: {bucket}")

key = "/".join(url.split("/")[3:])
print(f"key {key}")

s3 = boto3.client("s3")
obj = s3.get_object(Bucket=bucket, Key=key)
print(obj.get("Body").read().decode("utf-8"))
