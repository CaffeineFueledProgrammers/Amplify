"""
Amplify - AI-Powered Note-Taking for Students

This module contains all the routes for the Flask app.
"""

from flask import Flask, send_from_directory

from amplify_backend import app_factory

flask_app = app_factory.get_app()


@flask_app.route("/")
def landing_page():
    """
    The landing page of the application.
    """

    return send_from_directory(
        flask_app.static_folder, "index.html"  # type: ignore[reportArgumentType]
    )


def get_app_with_routes() -> Flask:
    """
    Returns the Flask app with all the routes.

    :returns Flask: The Flask app with all the routes.
    """

    return flask_app
