"""
Simple machine learning model training script based on an example given here:
https://medium.com/mantisnlp/mlops-with-sagemaker-44ffc2c1054a
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

# Load params

def load_data(split_data_path: str):
    """
    Load the split data files and return lists
    """
    files = {"X_train": [], "X_test": [], "y_train": [], "y_test": []}
    for k, v in files.items():
        file_path = os.path.join(split_data_path, f"{k}.txt")
        with open(file_path, "r") as f:
            files[k] = f.readlines()

    return files


@app.command()
def train(
        split_data_path: str = typer.Option(...),
        model_path: str = typer.Option(...),
        metrics_path: str = typer.Option(...),
        min_df: int = typer.Option(...),
        max_df: float = typer.Option(...),
        max_ngrams: int = typer.Option(...),
        stopwords: str = typer.Option(...),
        loss: str = typer.Option(...),
        learning_rate: float = typer.Option(...),
):
    """
    Trains the model and reports metrics to stdout

    Args:
        data: dict containing train and test split data
        split_data_path (str): Path to the split data
        model_path: path to save the model
        min_df: minimum number of documents a token must be found in for it to
            be included. Can be either an integer of actual documents or a
            float of the proportion of total documents.
        max_df: maximum number of documents a token can be found in before it
            is excluded. Can be either an integer of actual documents or a
            float of the proportion of total documents.
        max_ngrams: maximum n-grams to be used for the feature.
        stopwords: list of stopwords to be used.
        loss: loss function to be used.
        learning_rate: learning rate for the SGDClassifier.
    """

    data = load_data(split_data_path)

    model = Pipeline(
        [
            (
                "tfidf",
                TfidfVectorizer(
                    min_df=min_df,
                    ngram_range=(1, max_ngrams),
                    stop_words=stopwords
                ),
            ),
            ("svm", SGDClassifier(loss=loss, alpha=learning_rate)),
        ]
    )

    print("Training SGDClassifier")

    model.fit(data["X_train"], data["y_train"])

    print(f"Saving model to {model_path}")
    joblib.dump(model, model_path)



if __name__ == "__main__":
    app()
