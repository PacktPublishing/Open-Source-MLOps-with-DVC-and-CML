"""
Simple script to create train and test splits
"""

import csv
import os

import dvc.api
from sklearn.model_selection import train_test_split

# Load params

params = dvc.api.params_show()


def prepare_data(data_path: str, test_size: float):
    """
    Loads the data from the csv file and split it into train and test sets.

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


def save_data(output_path: str, **kwargs):
    """
    Saves train and test splits to disk
    """
    os.makedirs(output_path, exist_ok=True)

    for k, v in kwargs.items():
        output_file = os.path.join(output_path, f"{k}.txt")
        print(f"Saving {k} to {output_file}")
        with open(output_file, "w") as f:
            for item in v:
                f.write(item + "\n")


if __name__ == "__main__":
    X_train, X_test, y_train, y_test = prepare_data(
        data_path=params["data_path"],
        test_size=params["process"]["test_size"],
    )

    save_data(
        output_path=params["output_path"],
        X_train=X_train,
        X_test=X_test,
        y_train=y_train,
        y_test=y_test,
    )
