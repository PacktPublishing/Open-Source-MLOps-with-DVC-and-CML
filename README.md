# Open-Source-MLOPs-with-DVC-and-CML

## Model Metrics

| Path                 | score   |
|----------------------|---------|
| results/metrics.json | 0.891   |

## DAG

```mermaid
flowchart TD
	node1["data/IMDB_movie_ratings_sentiment.csv"]
	node2["data/processed/X_test.txt"]
	node3["data/processed/X_train.txt"]
	node4["data/processed/y_test.txt"]
	node5["data/processed/y_train.txt"]
	node6["models/model.joblib"]
	node7["results/metrics.json"]
	node1-->node2
	node1-->node3
	node1-->node4
	node1-->node5
	node2-->node6
	node2-->node7
	node3-->node6
	node3-->node7
	node4-->node6
	node4-->node7
	node5-->node6
	node5-->node7
```


