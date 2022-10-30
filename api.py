import os

import joblib
import dvc.api
from fastapi import FastAPI

REV = os.getenv("REV", "main")
REMOTE = os.getenv("REMOTE", "s3")
REMOTE_PATH = os.getenv("REMOTE_PATH", "models/model.joblib")
REPO = os.getenv(
    "REPO", "https://github.com/PacktPublishing/Open-Source-MLOps-with-DVC-and-CML.git"
)

# Load model from the cache

print(f"Loading model from {REMOTE_PATH} in {REV} revision")

with dvc.api.open(
    path=REMOTE_PATH,
    repo=REPO,
    rev=REV,
    remote=REMOTE,
    mode="rb",
) as fd:
    model = joblib.load(fd)

app = FastAPI()


@app.post("/predict")
def predict(data: dict):
    pred = model.predict([data["text"]])
    pred = pred[0].split("\n")[0]

    return {"class": pred}
