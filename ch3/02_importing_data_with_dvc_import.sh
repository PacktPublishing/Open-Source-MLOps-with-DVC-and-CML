
cd $PROJECT_PATH-registry

# Activate the virtual environment

source venv/bin/activate

# Add with dvc import

rm data/IMDB_movie_ratings_sentiment.csv

dvc import https://github.com/ivyleavedtoadflax/os-mlops-dvc-registry data/IMDB_movie_ratings_sentiment.csv -o data

git status

ls -lh data                          

cat data/IMDB_movie_ratings_sentiment.csv.dvc 

git commit -am 'Add data from registry'
