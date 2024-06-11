"""
Amplify - AI-Powered Note-Taking for Students

This module contains the database handler for the application.
"""

# pyright: reportAny=false

import hashlib
import random
from enum import Enum
from string import ascii_letters
from typing import Any

from amplify_backend import db_manager


class UserLevel(Enum):  # pylint: disable=C0115
    ADMIN = 0
    NORMAL = 1


def validate_password(password: str) -> dict[str, bool | str]:
    """
    Validate a given password.

    :param str password: The password to validate.
    :return bool: True if the password is valid, False otherwise.
    """

    if len(password) < 8:
        return {"status": False, "message": "Password must be at least 8 characters."}

    return {"status": True, "message": "Password is valid."}


def hash_password(password: str, salt: str) -> str:
    """
    Hash the password and return its hex digest.

    :param str password: The password to hash.
    :returns: The hashed password.
    """

    return hashlib.pbkdf2_hmac(
        "sha256", password.encode(), salt.encode(), iterations=100000, dklen=32
    ).hex()


class UserManager(db_manager.DatabaseManager):
    """
    This class handles all user-related operations.
    """

    def _run(self, query: str) -> list[Any]:
        cursor = self.database.cursor()
        _ = cursor.execute(query)
        return cursor.fetchall()

    def register_user(
        self, username: str, password: str, is_admin: bool = False
    ) -> int:
        """
        Register a new user in the database.

        Throws ValueError if the username already exists or the password is invalid.

        :param str username: The username of the user.
        :param str password: The password of the user.
        :param bool is_admin: Whether the user is an admin or not.
        :returns: The user ID of the registered user.
        """

        cursor = self.database.cursor()

        # Check if the password is valid.
        password_validation = validate_password(password)
        if not password_validation["status"]:
            raise ValueError(password_validation["message"])

        # Check if the username is in the database.
        _ = cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        if cursor.fetchone():
            raise ValueError("Username already exists.")

        # Hash the password.
        salt: str = "".join(random.choices(ascii_letters, k=16))
        password = hash_password(password, salt)

        _ = cursor.execute(
            "INSERT INTO users (username, password, is_admin, welcomed) VALUES (?, ?, ?, ?)",
            (username, ":".join((password, salt)), is_admin, False),
        )
        self.database.commit()

        if cursor.lastrowid is None:
            raise ValueError("Failed to register user.")

        return cursor.lastrowid

    def get_user_info(self, user_id: int) -> dict[str, str]:
        """
        Get a user's information.

        :param int user_id: the user ID of the user.
        :return dict[str, str]: The row from the database containing the user's information.
        """

        cursor = self.database.cursor()

        _ = cursor.execute("SELECT * FROM user_info WHERE user_id = ?", (user_id,))
        record: tuple[str, ...] | None = cursor.fetchone()
        if record is None:
            raise ValueError("User does not exist.")

        return {
            "user_id": record[0],
            "first_name": record[1],
            "last_name": record[2],
            "email": record[3],
            "phone_number": record[4],
            "address": record[5],
        }

    def update_user_info(self, user_id: int, **kwargs: dict[str, Any]) -> None:
        """
        Update the user's information.

        :param int user_id: The user ID of the user.
        """

        cursor = self.database.cursor()

        _ = cursor.execute("SELECT * FROM user_info WHERE user_id = ?", (user_id,))
        if cursor.fetchone():
            _ = cursor.execute(
                """
                UPDATE user_info
                SET first_name = ?, last_name = ?, email = ?, phone_number = ?, address = ?
                WHERE user_id = ?
                """,
                (
                    kwargs["first-name"],
                    kwargs["last-name"],
                    kwargs["email"],
                    kwargs["phone-number"],
                    kwargs["address"],
                    user_id,
                ),
            )
        else:
            _ = cursor.execute(
                """
                INSERT INTO user_info
                (user_id, first_name, last_name, email, phone_number, address)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (
                    user_id,
                    kwargs["first-name"],
                    kwargs["last-name"],
                    kwargs["email"],
                    kwargs["phone-number"],
                    kwargs["address"],
                ),
            )

        _ = cursor.execute(
            "UPDATE users SET welcomed = ? WHERE id = ?", (True, user_id)
        )
        self.database.commit()

    def validate_user(self, username: str, password: str) -> int | None:
        """
        Check if the username and their password is valid.

        :param str username: The username of the user.
        :param str password: The plaintext password of the user.
        :returns: The user ID if the username and password is valid, None otherwise.
        """

        cursor = self.database.cursor()

        _ = cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        record: tuple[int, str, str] | None = cursor.fetchone()
        if record is None:
            raise ValueError("Invalid username/password.")

        password = hash_password(password, record[2].partition(":")[2])

        if record[2].partition(":")[0] == password:
            return record[0]

        raise ValueError("Invalid username/password.")

    def get_user_level(self, user_id: int) -> UserLevel:
        """
        Get the user level of the user.
        """

        cursor = self.database.cursor()

        _ = cursor.execute("SELECT is_admin FROM users WHERE id = ?", (user_id,))
        record: tuple[int, str, str] | None = cursor.fetchone()
        if record is None:
            raise ValueError("User does not exist.")

        return UserLevel.ADMIN if record[0] else UserLevel.NORMAL

    def set_user_level(self, user_id: int, user_level: UserLevel) -> None:
        """
        Set the user level of the user.
        """

        cursor = self.database.cursor()

        _ = cursor.execute(
            "UPDATE users SET is_admin = ? WHERE id = ?",
            (user_level == UserLevel.ADMIN, user_id),
        )

        self.database.commit()

    def get_friends_list(self, user_id: int) -> list[int]:
        """
        Get a list of the user with ID <user_id>'s friends from the database.

        :param int user_id: The user ID
        :return list: A list of user IDs that are friends with the user.
        """

        cursor = self.database.cursor()

        _ = cursor.execute(
            """
            SELECT user_id2
            FROM friendships
            WHERE user_id1 = ?
            """,
            (user_id,),
        )

        return [record[0] for record in cursor.fetchall()]

    def get_all_users(self) -> list[dict[str, str]]:
        """
        Get a list of all users from the database.

        :return list: A list of user IDs.
        """

        cursor = self.database.cursor()

        _ = cursor.execute(
            """
            SELECT id
            FROM users
            """
        )

        return [self.get_user_info(record[0]) for record in cursor.fetchall()]
