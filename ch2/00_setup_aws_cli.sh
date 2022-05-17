
# Define the project folder you used in Chapter 1

PROJECT_PATH=~/Documents/my_project
S3_BUCKET=s3://os-mlops-dvc

# Make the folder

cd $PROJECT_PATH

# Activate the virtual environment

source venv/bin/activate
pip install awscli

# Now configure your account credentials with. This is commented out
# to make it easier to repeat these commands, as you only need to
# do it once. Uncomment this command if you are running this script
# for the first time.

# aws configure --profile $AWS_PROFILE

# Export the AWS_PROFILE environment variable to match to avoid
# needing to add --profile my_profile to every command.

export AWS_PROFILE=packt
