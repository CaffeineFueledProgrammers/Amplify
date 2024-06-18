"""
Amplify - AI-Powered Note-Taking for Students
"""

from dataclasses import dataclass

from amplify_backend.models.permission import Permission


@dataclass
class Note:
    """This class represents a user's note.

    Attributes:
        uid: The unique identifier of the note.
        version: The spec version of the note.
        content: The content of the note.
        is_public: Whether the note is publicly accessible or not.
        shared_to: A list of UIDs of users and their permissions
            who have access to the note.
    """

    uid: int
    version: int
    content: str
    is_public: bool
    shared_to: list[tuple[int, Permission]]
