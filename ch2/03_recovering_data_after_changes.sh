# Define the project folder you used in Chapter 1

PROJECT_PATH=~/Documents/my_project
S3_BUCKET=s3://os-mlops-dvc
AWS_PROFILE=packt

# Export the AWS_PROFILE env var so it can be read by awscli

export AWS_PROFILE=$AWS_PROFILE

# Navigate to the project folder

cd $PROJECT_PATH

# Activate the virtual environment

source venv/bin/activate

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

# Finally let's update our virtual environment since we installed awscli and 
# dvc[s3] in this chapter.

pip freeze > requirements.txt
git add requirements.txt
git commit -m 'Update dependencies'
