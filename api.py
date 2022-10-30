import os

import joblib
from dvc.api import DVCFileSystem
from fastapi import FastAPI

REV = os.getenv("REV", "main")
REMOTE = os.getenv("REMOTE", "s3")
LOCAL_PATH = os.getenv("LOCAL_PATH", "/tmp/model.joblib")
REMOTE_PATH = os.getenv("REMOTE_PATH", "models/model.joblib")
REPO = os.getenv(
    "REPO", "https://github.com/PacktPublishing/Open-Source-MLOps-with-DVC-and-CML.git"
)

# Load model artefacts from cache

fs = DVCFileSystem(REPO, rev=REV)
fs.get_file(REMOTE_PATH, LOCAL_PATH, remote=REMOTE)

print(f"Loading model from {LOCAL_PATH}")
model = joblib.load(LOCAL_PATH)

app = FastAPI()


@app.post("/predict")
def predict(data: dict):
    pred = model.predict([data["text"]])
    pred = pred[0].split("\n")[0]

    return {"class": pred}
