"""
Simple predictor script
"""

import argparse

import dvc.api
import joblib

params = dvc.api.params_show()


def predict(
    model_path: str,
    data_path: str,
    pred_path: str,
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


args = argparse.ArgumentParser()
args.add_argument("--model_path", type=str, default=params["model_path"])
args.add_argument("--data_path", type=str)
args.add_argument("--pred_path", type=str)


if __name__ == "__main__":

    args = args.parse_args()

    predict(
        model_path=args.model_path,
        data_path=args.data_path,
        pred_path=args.pred_path,
    )
