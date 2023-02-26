"""
Simple evaluation script
"""

import argparse
import json

import dvc.api
import sklearn.metrics as metrics

# Load params

params = dvc.api.params_show()


def evaluate(
    pred_path: str,
    true_path: str,
    metrics_path: str,
):
    """
    Evaluate predictions against the true labels, and save the metrics to a
    file.

    Args:
        pred_path (str): Path to the predictions.
        true_path (str): Path to the true labels.
        metrics_path (str): Path to save the metrics.

    Returns:
        None
    """

    preds = []

    print(f"Reading predictions from {pred_path}")
    with open(pred_path) as f:
        for line in f:
            preds.append(line.strip())

    true = []

    print(f"Reading true labels from {true_path}")
    with open(true_path) as f:
        for line in f:
            true.append(line.strip())

    results = metrics.classification_report(true, preds, output_dict=True)

    with open(metrics_path, "w") as fd:
        json.dump(results, fd, indent=4)
    print(f"Saved metrics to {metrics_path}")


args = argparse.ArgumentParser()
args.add_argument("--pred_path", type=str)
args.add_argument("--true_path", type=str)
args.add_argument("--metrics_path", type=str)


if __name__ == "__main__":

    args = args.parse_args()

    evaluate(
        pred_path=args.pred_path,
        true_path=args.true_path,
        metrics_path=args.metrics_path,
    )
