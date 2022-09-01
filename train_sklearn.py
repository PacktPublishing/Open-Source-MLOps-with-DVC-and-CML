"""
Simple machine learning model training script based on an example given here:
https://medium.com/mantisnlp/mlops-with-sagemaker-44ffc2c1054a
"""

import csv
import os

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split


def prepare_data(data_path: str, test_size: float ):
    """
    A simple function to load the data from the csv file and split it into
    training and testing sets.

    Args:
        data_path: path to the csv file containing the data.
        test_size: proportion of the data to be used for testing.
    """
    data = []
    print(f"Loading data from {data_path}")
    with open(data_path, encoding="utf-8-sig") as f:
        csvreader = csv.DictReader(f)
        for row in csvreader:
            data.append((row["text"], row["label"]))
    X, y = zip(*data)
    print(f"Loaded {len(X)} examples")

    print("Splitting data into train and test sets")

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size)

    print(f"Train set size: {len(X_train)}")
    print(f"Test set size: {len(X_test)}")

    return X_train, X_test, y_train, y_test


def train(
        data_path: str,
        min_df: int = 5,
        max_df: float = 0.5,
        max_ngrams: int = 1,
        stopwords: str="english",
        loss: str="hinge",
        learning_rate: float = 1e-4,
        test_size: float = 0.2,
):
    """
    Trains the model and reports metrics to stdout

    Args:
        data_path: path to the csv file containing the data
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
        test_size: proportion of the data to be used for testing.
    """

    X_train, X_test, y_train, y_test = prepare_data(data_path, test_size=test_size)

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

    model.fit(X_train, y_train)

    score = model.score(X_test, y_test)

    print(f"Model score {score}")


if __name__ == "__main__":
    train(data_path="data/IMDB_movie_ratings_sentiment.csv")
