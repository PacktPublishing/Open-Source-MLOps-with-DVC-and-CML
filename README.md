# Open Source MLOPS with DVC and CML

## A note on virtual environments

Since starting to write the book in early 2022 there have been a lot of changes to the open source depdendencies that this project relies on. In order to ensure that a reproducible environment is available for readers across platforms, I have set up a virtual environment in [poetry](https://python-poetry.org/) which can be used to install the dependencies for this project as an alternative to the way described in the book, which uses `pip`. The get started with poetry, you can follow the instructions [here](https://python-poetry.org/docs/#installing-with-pipx). I recommend installing poetry using `pipx` as described in the link above. Note that this virtual environment contains all the dependencies that you will encounter in the book, so you can safely ignore any instructions to install packages in the code examples in the book.

Once you have poetry installed, you can install the dependencies for this project by running the following command from the root of the project:

```bash
poetry install
```

To create a shell with the virtual environment activated, run the following command:

```bash
poetry shell
```

## Model Metrics

| Path                 | score   |
|----------------------|---------|
| results/metrics.json | 0.891   |

## DAG

This shows the Directed Acyclic Graph (DAG) for the current project pipeline.

```mermaid
flowchart TD
	node1["data/IMDB_movie_ratings_sentiment.csv"]
	node2["data/predictions/y_test_pred.txt"]
	node3["data/predictions/y_train_pred.txt"]
	node4["data/processed/X_test.txt"]
	node5["data/processed/X_train.txt"]
	node6["data/processed/y_test.txt"]
	node7["data/processed/y_train.txt"]
	node8["models/model.joblib"]
	node9["results/test_metrics.json"]
	node10["results/train_metrics.json"]
	node1-->node4
	node1-->node5
	node1-->node6
	node1-->node7
	node2-->node9
	node3-->node10
	node4-->node2
	node4-->node8
	node5-->node3
	node5-->node8
	node6-->node8
	node6-->node9
	node7-->node8
	node7-->node10
	node8-->node2
	node8-->node3
```
