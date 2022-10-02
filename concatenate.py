"""
Reads in actual and predicted data and saves them out to a single csv file for
use with dvc plots
"""

import argparse

def concatenate(
    true_labels: str,
    predicted_labels: str,
    output_path: str,
):
    """Concatenate true and predicted labels into a single csv file"""

    true = []
    pred = []

    with open(true_labels, "r") as f:
        for line in f:
            true.append(line.strip())

    with open(predicted_labels, "r") as f:
        for line in f:
            pred.append(line.strip())

    with open(output_path, "w") as f:
        f.write("true,pred\n")

        for true, pred in zip(true, pred):
            f.write(f"{true},{pred}\n")

args = argparse.ArgumentParser()
args.add_argument("--true_labels", type=str)
args.add_argument("--predicted_labels", type=str)
args.add_argument("--output_path", type=str)

if __name__ == "__main__":
    args = args.parse_args()
    concatenate(
        args.true_labels,
        args.predicted_labels,
        args.output_path,
    )
