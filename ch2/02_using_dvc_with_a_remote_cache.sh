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

# Install dependencies required for working with S3

pip install 'dvc[s3]'

# Now push our local cash to the remote

dvc push

# Introspect our local cache

tree -s ./dvc/cache

# Check what files are in the remote

aws s3 ls $S3_BUCKET/

# Push data from _all_ commits.

dvc push --all-commits

# Check again what files are in the remote.

aws s3 ls $S3_BUCKET/
