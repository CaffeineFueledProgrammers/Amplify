"""
Amplify - AI-Powered Note-Taking for Students

This module contains the database handler for the application.
"""

import sqlite3

from amplify_backend import config


class DatabaseManager:  # pylint: disable=R0903
    """
    This class contains the low-level database operations, and
    serves as a base class for other classes that need to interact
    with the database.
    """

    def __init__(self) -> None:
        self.database = sqlite3.connect(config.Config.DATABASE_URI)

    def initialize_database(self) -> None:
        """
        Create the database.
        """

        cursor = self.database.cursor()
        _ = cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                is_admin BOOLEAN NOT NULL,
                welcomed BOOLEAN NOT NULL
            )
            """
        )
        _ = cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS user_info (
                user_id INTEGER PRIMARY KEY,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                email TEXT,
                phone_number TEXT,
                address TEXT,
                FOREIGN KEY(user_id) REFERENCES users(id)
            )
            """
        )
        _ = cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                content TEXT NOT NULL,
                date_created DATETIME DEFAULT CURRENT_TIMESTAMP,
                last_modified DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY(user_id) REFERENCES users(id)
            )
            """
        )

        self.database.commit()

    def close(self) -> None:
        """
        Close the database connection.
        """
        self.database.close()
