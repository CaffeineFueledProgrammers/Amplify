"""
Amplify - AI-Powered Note-Taking for Students
"""

from dataclasses import dataclass


@dataclass
class User:
    """This class represents a user.

    Attributes:
        uid: The unique identifier of the user.
        username: The chosen username of the user.
        password: The hashed password of the user.
        is_admin: A boolean indicating if the user is an administrator.
        notes: A list of UIDs of notes owned by the user.
    """

    uid: int
    username: str
    password: str
    is_admin: bool
    notes: list[int]
