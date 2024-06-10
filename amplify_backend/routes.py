"""
Amplify - AI-Powered Note-Taking for Students

This module contains all the routes for the Flask app.
"""

from flask import Flask

flask_app = Flask(__name__)


@flask_app.route("/")
def landing_page():
    """
    The landing page of the application.
    """

    return "Hello, Amplify!"


def get_app() -> Flask:
    """
    Returns the Flask app with all the routes.

    :returns Flask: The Flask app with all the routes.
    """

    return flask_app
