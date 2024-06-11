"""
Amplify - AI-Powered Note-Taking for Students

Get the Flask app
"""

from flask import Flask

from amplify_backend.config import BaseConfig


def get_app() -> Flask:
    """
    Get the Flask app instance.
    """

    return Flask(
        BaseConfig.NAME, static_folder=BaseConfig.STATIC_DIR, static_url_path=""
    )
