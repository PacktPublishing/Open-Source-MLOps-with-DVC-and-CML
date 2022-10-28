import joblib
from fastapi import FastAPI

# Load the model from disk

model = joblib.load("models/model.joblib")

# Initialize the app

app = FastAPI()

# Add a predict endpoint


@app.post("/predict")
def predict(data: dict):
    pred = model.predict([data["text"]])
    pred = pred[0].split("\n")[0]
    return {"class": pred}
