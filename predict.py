"""
Simple predictor script
"""

import csv
import os
import joblib
import json
import typer

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline

# Create typer app

app = typer.Typer()


@app.command()
def predict(
        model_path: str = typer.Option(...),
        data_path: str = typer.Option(...),
        pred_path: str = typer.Option(...),
):
    """
    Make predictions on an arbitrary dataset using a trained model

    Args:
        model_path (str): Path to the trained model
        data_path (str): Path to the data to make predictions on
        pred_path (str): Path to save the predictions to
    """

    # Load the model
    model = joblib.load(model_path)

    # Load the txt data to make predictions on

    data = []

    with open(data_path, "r") as f:
        for line in f:
            data.append(line.strip())

    # Make predictions

    predictions = model.predict(data)

    # Save the predictions to disk

    with open(pred_path, "w") as f:
        for pred in predictions:
            f.write(pred)


if __name__ == "__main__":
    app()
