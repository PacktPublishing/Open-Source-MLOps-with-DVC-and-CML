# Define the project folder we will use for Chapter 1

PROJECT_PATH=~/Documents/my_project

cd $PROJECT_PATH

# Download the zipped data from github using curl. You can also use another
# tool or follow the link to do this manually.

curl -L https://github.com/PacktPublishing/Open-Source-MLOPs-with-DVC-and-CML/raw/chapter/1/ch1/IMDB_movie_ratings_sentiment.zip > $PROJECT_PATH/IMDB_movie_ratings_sentiment.zip

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
