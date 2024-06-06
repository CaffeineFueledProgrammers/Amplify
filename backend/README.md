# Amplify

This directory contains the backend of Amplify.

## Requirements

-   Python >= 3.10
-   Poetry >= 1.8.3

## Setup

### Development

```bash
python3 -m venv venv        # create a virtual environment.
source ./venv/bin/activate  # activate the virtual environment.
poetry install              # install the requirements.

# make database migrations
python manage.py makemigrations
python manage.py migrate

# create admin account
python manage.py createsuperuser

cd amplify
# This step is not required anymore.
# export AMPLIFY_SECRET_KEY=$(cat ../secrets.env)  # export the secret key
python manage.py runserver 0.0.0.0:8080          # run the development server
```
