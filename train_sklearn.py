"""
Simple machine learning model training script based on an example given here:
https://medium.com/mantisnlp/mlops-with-sagemaker-44ffc2c1054a
"""

import os

import dvc.api
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline

# Load params

params = dvc.api.params_show()


def load_data(split_data_path):
    """
    Load the split data files and return lists
    """
    files = {"X_train": [], "X_test": [], "y_train": [], "y_test": []}

    for k, v in files.items():
        file_path = os.path.join(split_data_path, f"{k}.txt")
        with open(file_path, "r") as f:
            files[k] = f.readlines()

    return files


def train(
    data: dict,
    model_path: str,
    min_df: int,
    max_df: float,
    max_ngrams: int,
    stopwords: str,
    loss: str,
    learning_rate: float,
):
    """
    Trains the model and reports metrics to stdout

    Args:
        data: dict containing train and test split data
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

    model = Pipeline(
        [
            (
                "tfidf",
                TfidfVectorizer(
                    min_df=min_df, ngram_range=(1, max_ngrams), stop_words=stopwords
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
    split_data = load_data(params["output_path"])
    train(
        data=split_data,
        model_path=params["model_path"],
        min_df=params["train"]["min_df"],
        max_df=params["train"]["max_df"],
        max_ngrams=params["train"]["max_ngrams"],
        stopwords=params["train"]["stopwords"],
        loss=params["train"]["loss"],
        learning_rate=params["train"]["learning_rate"],
    )
