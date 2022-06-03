
cd $PROJECT_PATH-registry

# Activate the virtual environment

source venv/bin/activate

dvc update data/IMDB_movie_ratings_sentiment.csv.dvc

dvc status

git status

wc -l data/*.csv

cat data/IMDB_movie_ratings_sentiment.csv.dvc

git commit  update data/IMDB_movie_ratings_sentiment.csv.dvc

git commit data/IMDB_movie_ratings_sentiment.csv.dvc -m 'Update to latest data'
