"""
Reads in actual and predicted data and saves them out to a single csv file for
use with dvc plots
"""

import typer

app = typer.Typer()


@app.command()
def concatenate(
    true_labels: str = typer.Option(..., help="Path to true labels"),
    predicted_labels: str = typer.Option(..., help="Path to predicted labels"),
    output_path: str = typer.Option(..., help="Path to output file"),
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


if __name__ == "__main__":
    app()
