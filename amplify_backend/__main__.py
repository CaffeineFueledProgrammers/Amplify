"""
Amplify - AI-Powered Note-Taking for Students
"""

from amplify_backend.config import Config
from amplify_backend.routes import get_app


def main():
    """
    The main function of the application.
    """

    flask_app = get_app()
    flask_app.run(host=Config.HOST, port=Config.PORT, debug=True)


if __name__ == "__main__":
    main()
