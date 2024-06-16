"""
Amplify - AI-Powered Note-Taking for Students

This module contains all the routes for the Flask app.
"""

from flask import Flask, request, send_from_directory

from amplify_backend import config, user_manager

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

    try:
        username: str = request.json.get("username", None)  # type: ignore[reportAny]
        password: str = request.json.get("password", None)  # type: ignore[reportAny]
        if not username or not password:
            return {"message": "Invalid request"}, 400

        new_user_id = user_manager.UserManager().register_user(username, password)
        return (
            {"message": "OK", "user_id": new_user_id, "username": username},
            200,
        )

    except ValueError as e:
        return {"message": str(e)}, 400

    except Exception as e:  # pylint: disable=W0718
        return {"message": str(e)}, 500


# API Endpoints
@flask_app.route("/api/v1/user/auth/login", methods=["POST"])
def api_v1_user_auth_login():
    """
    Logs in an existing user.
    """

    try:
        username: str = request.json.get("username", None)  # type: ignore[reportAny]
        password: str = request.json.get("password", None)  # type: ignore[reportAny]
        if not username or not password:
            return {"message": "Invalid request"}, 400

        user_id = user_manager.UserManager().validate_user(username, password)
        return {"message": "OK", "user_id": user_id, "username": username}, 200

    except ValueError as e:
        return {"message": str(e)}, 400


def get_app() -> Flask:
    """
    Returns the Flask app with all the routes.

    :returns Flask: The Flask app with all the routes.
    """

    return flask_app
