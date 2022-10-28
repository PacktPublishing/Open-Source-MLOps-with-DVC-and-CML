"""
Chapter 10: Deploying Models with DVC

Example of reading a file using dvc.api.open from Chapter 10.
"""
import dvc.api
import json

with dvc.api.open(
    path="results/train_metrics.json",
    repo="https://github.com/PacktPublishing/Open-Source-MLOps-with-DVC-and-CML.git",
    rev="chapter-09",
    remote="s3",
    mode="rb",
    encoding="utf-8",
) as fd:
    print(json.load(fd))

# to save to disk:

with dvc.api.open(
    path="results/train_metrics.json",
    repo="https://github.com/PacktPublishing/Open-Source-MLOps-with-DVC-and-CML.git",
    rev="chapter-09",
    remote="s3",
    mode="rb",
    encoding="utf-8",
) as remote_file:
    with open("/tmp/train_metrics.json", "wb") as local_file:
        remote_file_contents = remote_file.read()
        local_file.write(remote_file_contents)
