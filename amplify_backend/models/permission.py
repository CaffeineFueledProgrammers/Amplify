"""
Amplify - AI-Powered Note-Taking for Students
"""

from enum import Enum


class Permission(Enum):
    """This class represents a user's permission level for a note.

    Attributes:
        VIEW_ONLY: The user can only view the note.
        EDIT: The user can edit the note.
        OWNER: The user can edit, delete, and share the note.
    """

    VIEW_ONLY = 0
    EDIT = 1
    OWNER = 2
