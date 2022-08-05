
# Navigate to the project folder

cd $PROJECT_PATH
source $PROJECT_PATH/venv/bin/activate

# Install dependencies required for working with S3

pip install 'dvc[s3]'

# Now push our local cash to the remote

dvc push

# Introspect our local cache

tree -s ./dvc/cache

# Check what files are in the remote

aws s3 ls s3://$S3_BUCKET/

# Push data from _all_ commits.

dvc push --all-commits

# Check again what files are in the remote.

aws s3 ls s3://$S3_BUCKET/
