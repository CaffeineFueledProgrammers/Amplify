"""
Amplify - AI-Powered Note-Taking for Students
"""

from amplify_backend import config
from amplify_backend.app import get_app


def main():
    """
    The main function of the application.
    """

    flask_app = get_app()
    flask_app.run(
        host=config.Config.HOST, port=config.Config.PORT, debug=config.Config.DEBUG
    )


if __name__ == "__main__":
    main()
