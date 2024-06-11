"""
Amplify - AI-Powered Note-Taking for Students

This file is used to store all the configuration
variables that are used in the application.
"""

import os


class BaseConfig:  # pylint: disable=too-few-public-methods,missing-class-docstring
    # Server configuration
    HOST = "0.0.0.0"
    PORT = 8081
    SECRET_KEY = os.getenv("AMPLIFY_SECRET_KEY", os.urandom(32).hex())

    DEBUG = False
    TESTING = False

    # Flask configuration
    NAME = "Amplify"
    STATIC_DIR = "./amplify_frontend/dist"  # NOTE: Is this the right place?


class DevConfig(
    BaseConfig
):  # pylint: disable=too-few-public-methods,missing-class-docstring
    DEBUG = True
    TESTING = False

    # Database configuration
    DATABASE_URI = os.getenv("AMPLIFY_DATABASE_URI", "sqlite:///data/amplify_local.db")


class TestConfig(
    BaseConfig
):  # pylint: disable=too-few-public-methods,missing-class-docstring
    DEBUG = True
    TESTING = True

    # Database configuration
    DATABASE_URI = os.getenv("AMPLIFY_DATABASE_URI", "sqlite:///data/amplify_test.db")


class ProdConfig(
    BaseConfig
):  # pylint: disable=too-few-public-methods,missing-class-docstring
    DEBUG = False

    # Database configuration
    DATABASE_URI = os.getenv("AMPLIFY_DATABASE_URI", "sqlite:///data/amplify.db")
