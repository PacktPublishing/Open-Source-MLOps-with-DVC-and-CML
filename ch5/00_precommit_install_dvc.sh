
# Navigate to the project folder

cd $PROJECT_PATH

# Activate the virtual environment

source venv/bin/activate

# Install pre-commit

pip install pre-commit

# Install the dvc hooks

dvc install --use-pre-commit-tool

# Add pre-commit to our dependencies

pip freeze > requirements.txt
git commit -m "Update dependencies" requirements.txt

# Add pre commit config and requirements.txt to git

git add .pre-commit-config.yaml
git commit -m 'Add pre-commit config'
