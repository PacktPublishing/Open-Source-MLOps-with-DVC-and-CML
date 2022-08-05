
# Navigate to folder and activate the virtual environment

cd $PROJECT_PATH
source $PROJECT_PATH/venv/bin/activate

# Download the zipped data from GitHub using curl. You can also use another
# tool or follow the link to do this manually.

curl -L https://github.com/PacktPublishing/Open-Source-MLOPs-with-DVC-and-CML/blob/ce1fd2e5205b92d8c16e449e3fb2a67f380b6dde/ch1/IMDB_movie_ratings_sentiment.zip?raw=true > $PROJECT_PATH/IMDB_movie_ratings_sentiment.zip

# Make a new folder in which to store the data

mkdir -p data

# Unzip the data and move into the data folder

unzip IMDB_movie_ratings_sentiment.zip
mv IMDB_movie_ratings_sentiment.csv data

# Add the data file to DVC

dvc add data/IMDB_movie_ratings_sentiment.csv

# Add the newly created files to DVC. These are the .dvc file which tracks the
# file's hash digest, and a folder specific .gitignore file which will force git
# to ignore the data file.

git add data/IMDB_movie_ratings_sentiment.csv.dvc data/.gitignore

# Let's commit both of these new files to Git

git commit -m "Add raw data to dvc"

# Finally we delete the zip file, which we no longer need.

rm $PROJECT_PATH/IMDB_movie_ratings_sentiment.zip
