"""
Amplify - AI-Powered Note-Taking for Students

This file is used to store all the configuration
variables that are used in the application.
"""

import os


class Config:  # pylint: disable=too-few-public-methods,missing-class-docstring
    # Server configuration
    HOST = os.getenv("AMPLIFY_HOST", "0.0.0.0")
    PORT = int(os.getenv("AMPLIFY_PORT", "8081"))
    SECRET_KEY = os.getenv("AMPLIFY_SECRET_KEY", os.urandom(32).hex())

    DEBUG = os.getenv("AMPLIFY_DEBUG", "false") == "true"
    TESTING = os.getenv("AMPLIFY_TESTING", "false") == "true"
    LOGFILEPATH = "amplify.log"

    # Flask configuration
    NAME = "Amplify"
    STATIC_DIR = "./amplify_frontend/dist"  # NOTE: Is this the right place?

    # Database configuration
    DATABASE_URI = os.getenv("AMPLIFY_DATABASE_URI", "sqlite:///data/amplify.db")
