# Define the project folder we will use for Chapter 1

PROJECT_PATH=~/Documents/mantis/books/os-mlops-dvc

# Make the folder

mkdir -p $PROJECT_PATH
cd $PROJECT_PATH

# Initialise a git repository

git init
git checkout -b main

# Create a virtual environment using python venv and activate it

python3 -m venv venv
source venv/bin/activate

# Install dvc and initialize a dvc repository

pip install dvc
dvc init

# Add a .gitignore

echo venv > .gitignore

# Create a requirements.txt file

pip freeze > requirements.txt

# Make the first git commit

git add .gitignore requirements.txt
git commit -am 'ch2 00 Create a Virtuale Environment'
