"""
Chapter 10: Deploying Models with DVC

Example of reading a file usDVCFileSystem.
"""
from dvc.api import DVCFileSystem

url = "https://github.com/PacktPublishing/Open-Source-MLOps-with-DVC-and-CML.git"
fs = DVCFileSystem(url, rev="chapter-09")

with fs.open("results/train_metrics.json", "r") as f:
    print(f.read())

# To save to disk

fs.get_file("results/train_metrics.json", "/tmp/train_metrics.json")
