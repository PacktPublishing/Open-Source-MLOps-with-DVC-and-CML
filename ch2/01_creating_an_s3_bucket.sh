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

# Create your S3 Bucket

aws s3 mb $S3_BUCKET

# Check that the bucket was created

aws s3 ls $S3_BUCKET

# Add the bucket as a remote cache

dvc remote add s3 s3://os-mlops-dvc --default

# Commit the change to github

git add .dvc/config
git commit -m 'Add s3 remote cache'
