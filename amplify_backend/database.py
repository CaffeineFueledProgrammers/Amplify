"""
Amplify - AI-Powered Note-Taking for Students
"""

from sqlalchemy import create_engine

from amplify_backend import info


def get_db_engine():
    """Returns an SQLAlchemy engine for the database.

    Returns:
        The SQLAlchemy engine for the database.
    """

    return create_engine(info.DATABASE_URL)
