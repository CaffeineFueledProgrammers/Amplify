"""
Amplify - AI-Powered Note-Taking for Students

This module contains all the routes for the Flask app.
"""

from flask import Flask, send_from_directory

from amplify_backend import config

flask_app = Flask(
    config.Config.NAME, static_folder=config.Config.STATIC_DIR, static_url_path=""
)


# Routes
@flask_app.route("/")
def landing_page():
    """
    The landing page of the application.
    """

    return send_from_directory(
        flask_app.static_folder, "index.html"  # type: ignore[reportArgumentType]
    )


# API Endpoints
@flask_app.route("/api/v1/user/auth/register", methods=["POST"])
def api_v1_user_auth_register():
    """
    Registers a new user.
    """

    return {"message": "OK"}


# API Endpoints
@flask_app.route("/api/v1/user/auth/login", methods=["POST"])
def api_v1_user_auth_login():
    """
    Logs in an existing user.
    """

    return {"message": "OK"}


def get_app() -> Flask:
    """
    Returns the Flask app with all the routes.

    :returns Flask: The Flask app with all the routes.
    """

    return flask_app
