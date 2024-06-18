"""
Amplify - AI-Powered Note-Taking for Students
"""

from dataclasses import dataclass


@dataclass
class User:
    """This class represents a user.

    Attributes:
        id: The unique identifier of the user.
        username: The chosen username of the user.
        password: The hashed password of the user.
    """

    uid: int
    username: str
    password: str
