
# Navigate to the project folder and activate the virtual environment

cd $PROJECT_PATH
source $PROJECT_PATH/venv/bin/activate

# What happens when we delete the data from ./data?

rm data/IMDB_movie_ratings_sentiment.csv

# Check what dvc thinks about that

dvc status

# Recover the deleted file from dvc's local cache

dvc checkout

# Check DVC status again

dvc status

# Check the contents of ./data

tree data

# Now let's try again, but this time deleting our dvc cache and the data file
# in our local workspace.

rm -r data/IMDB_movie_ratings_sentiment.csv .dvc/cache
dvc status

# Now let's pull and check the status

dvc pull
tree data
tree .dvc/cache

# We don't need to commit anything here, as we didn't make any changes.
