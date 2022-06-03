
cd $PROJECT_PATH-registry

# Activate the virtual environment

source venv/bin/activate

curl -L https://github.com/PacktPublishing/Open-Source-MLOPs-with-DVC-and-CML/blob/f2623766827908ffeaa8cfc752ca21d18559c0a0/ch1/IMDB_movie_ratings_sentiment.zip?raw=true > ./IMDB_movie_ratings_sentiment.zip

unzip -o IMDB_movie_ratings_sentiment.zip -d data

rm IMDB_movie_ratings_sentiment.zip

dvc add data/IMDB_movie_ratings_sentiment.csv

git commit data/IMDB_movie_ratings_sentiment.csv.dvc -m ‘Update data’

dvc push 

git push



dvc update data/IMDB_movie_ratings_sentiment.csv.dvc

dvc status

git status

wc -l data/*.csv

cat data/IMDB_movie_ratings_sentiment.csv.dvc

git commit  update data/IMDB_movie_ratings_sentiment.csv.dvc

git commit data/IMDB_movie_ratings_sentiment.csv.dvc -m 'Update to latest data'
