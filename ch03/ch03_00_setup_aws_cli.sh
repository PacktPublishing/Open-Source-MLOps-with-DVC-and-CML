
# Navigate the the folder and activate the virtual environment

cd $PROJECT_PATH
source $PROJECT_PATH/venv/bin/activate

pip install awscli

# Now configure your account credentials with. This is commented out
# to make it easier to repeat these commands, as you only need to
# do it once. Uncomment this command if you are running this script
# for the first time.

# aws configure --profile $AWS_PROFILE

# Export the AWS_PROFILE environment variable to match to avoid
# needing to add --profile my_profile to every command.

export AWS_PROFILE=packt

# Add awscli to requirements.txt and commit to git

pip freeze > requirements.txt
git commit -m 'ch03 00 Set up aws cli' requirements.txt
