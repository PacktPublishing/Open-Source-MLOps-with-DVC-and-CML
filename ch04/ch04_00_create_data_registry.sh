# Variables that need to be exported into your environment for this script to
# run:
#
# AWS_PROFILE=default
# S3_BUCKET=s3://my-bucket
# PROJECT_PATH=/path/to/project
# PROJECT_NAME=os-mlops-dvc
# GITHUB_USER=ivyleavedtoadflax
#
# Values are provided as examples, and should be set according to the
# configuration on your individual machine.

source $PROJECT_PATH/venv/bin/activate

gh repo create \
    -–license MIT \
    -–public $GITHUB_USER/$PROJECT_NAME-registry

gh repo clone $GITHUB_USER/$PROJECT_NAME-registry

cd $PROJECT_NAME-registry

dvc init

git commit .dvc .dvcignore -m 'dvc init'

mkdir -p data

curl -L https://github.com/PacktPublishing/Open-Source-MLOPs-with-DVC-and-CML/blob/ce1fd2e5205b92d8c16e449e3fb2a67f380b6dde/ch1/IMDB_movie_ratings_sentiment.zip?raw=true > ./IMDB_movie_ratings_sentiment.zip

unzip IMDB_movie_ratings_sentiment.zip -d ./data

dvc add data/IMDB_movie_ratings_sentiment.csv

git add data/IMDB_movie_ratings_sentiment.csv.dvc data/.gitignore

rm IMDB_movie_ratings_sentiment.zip

git commit -m 'Add raw data to dvc'

git push

aws s3 mb s3://$S3_bucket-registry

dvc remote add --default s3 s3://$S3_BUCKET-registry 

git add .dvc/config 

git commit -m 'Add remote cache'

git push

dvc push
