
cd $PROJECT_PATH-registry

# Activate the virtual environment

source venv/bin/activate

dvc unprotect data/IMDB_movie_ratings_sentiment.csv

rm data/IMDB_movie_ratings_sentiment.csv data/.gitignore

git rm data/IMDB_movie_ratings_sentiment.csv.dvc

git commit data -m 'Remove IMDB data from local cache'	

# Get new data

dvc list --recursive https://github.com/ivyleavedtoadflax/$PROJECT_NAME-registry 

dvc get https://github.com/ivyleavedtoadflax/os-mlops-dvc-registry data/IMDB_movie_ratings_sentiment.csv -o data

dvc status

git status

ls -lh 
