
cd $PROJECT_PATH

# Create a new branch

git checkout -b data_update

# As before, download the zipped data from github using curl

curl -L https://github.com/PacktPublishing/Open-Source-MLOPs-with-DVC-and-CML/blob/f2623766827908ffeaa8cfc752ca21d18559c0a0/ch1/IMDB_movie_ratings_sentiment.zip?raw=true > $PROJECT_PATH/IMDB_movie_ratings_sentiment.zip

# Unzip the data and move into the data folder, and remove the zip file

unzip IMDB_movie_ratings_sentiment.zip

mv IMDB_movie_ratings_sentiment.csv data

rm $PROJECT_PATH/IMDB_movie_ratings_sentiment.zip

# Add the updated data file to dvc

dvc add data/IMDB_movie_ratings_sentiment.csv

cat data/IMDB_movie_ratings_sentiment.csv.dvc

git commit data/IMDB_movie_ratings_sentiment.csv.dvc -m 'Update data file'


echo "*** Reverting changes to original version ***"
git checkout main
dvc checkout 
tree -s data

echo "*** Switching to updated data ***"
git checkout data_update
dvc checkout
tree -s data

echo "*** Merging data_updates into main ***"
git checkout main
git merge data_update

echo "*** DVC checkout the previous data from detached head ***"
git checkout HEAD~1
dvc checkout
tree -s data

echo "*** Switch back to main ***"
git checkout main
dvc checkout
tree -s data
