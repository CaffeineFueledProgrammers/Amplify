# Amplify

This directory contains the backend of Amplify.

## Requirements

-   Python 3.12
-   Poetry 1.8.3

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

# run the development server
cd amplify
python manage.py runserver 0.0.0.0:8080
```
