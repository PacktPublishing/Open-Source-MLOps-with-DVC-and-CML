# Variables that need to be exported into your environment for this script to
# run:
#
# AWS_PROFILE=default
# S3_BUCKET=s3://my-bucket
# PROJECT_PATH=/path/to/project
#
# Values are provided as examples, and should be set according to the
# configuration on your individual machine.

# Navigate to the project folder and activate the virtual environment

cd $PROJECT_PATH
source $PROJECT_PATH/venv/bin/activate

# Create your S3 Bucket. This will fail if it has already been created, or if
# someone has already registered a bucket with the same name!

aws s3 mb s3://$S3_BUCKET

# Check that the bucket was created

aws s3 ls s3://$S3_BUCKET

# Add the bucket as a remote cache

dvc remote add s3 s3://$S3_BUCKET --default

# Commit the change to github

git add .dvc/config
git commit -m 'Add s3 remote cache'
