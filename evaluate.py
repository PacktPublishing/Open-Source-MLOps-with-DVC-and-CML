"""
Simple evaluation script
"""

import sklearn.metrics as metrics
import typer
import json

app = typer.Typer()

@app.command()
def evaluate(
    pred_path: str = typer.Option(...),
    true_path: str = typer.Option(...),
    metrics_path: str = typer.Option(...),
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


if __name__ == "__main__":
    app()
