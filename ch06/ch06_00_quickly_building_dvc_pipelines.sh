#   ch06_00_quickly_building_dvc_pipelines.sh
#   
#   In this script we will create a simple machine learning pipeline based on 
#   the example given here: <Del>
#
#

# Navigate to the project folder

# Copy the files we need to the project folder

cp train_sklearn.py $PROJECT_PATH

cd $PROJECT_PATH

# Activate the virtual environment

source $PROJECT_PATH/venv/bin/activate

# Install dependencies required for machine learning example

pip install sklearn

pip freeze > requirements.txt
