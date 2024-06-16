#!/usr/bin/env python
"""
Amplify - AI-Powered Note-Taking for Students
"""

from pathlib import Path

from amplify_backend import config, db_manager
from amplify_backend.app import get_app


def main():
    """
    The main function of the application.
    """

    flask_app = get_app()

    if not Path(config.Config.DATABASE_URI).exists():
        print("Database does not exist. Creating it now.")
        db_manager.DatabaseManager().initialize_database()

    flask_app.run(
        host=config.Config.HOST, port=config.Config.PORT, debug=config.Config.DEBUG
    )


if __name__ == "__main__":
    main()
