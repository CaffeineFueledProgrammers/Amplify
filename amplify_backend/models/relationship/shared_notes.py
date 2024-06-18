"""
Amplify - AI-Powered Note-Taking for Students
"""

# pylint: disable=R0903

from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from amplify_backend.models.base import Base
from amplify_backend.models.property.permission import Permission


class SharedNote(Base):
    """This class represents the relationship between a note and a user.

    Attributes:
        note_uid: The unique identifier of the note.
        shared_with: The unique identifier of the user with whom the note is shared.
    """

    __tablename__: str = "shared_notes"

    note_uid: Mapped[int] = mapped_column(ForeignKey("notes.uid"), primary_key=True)
    shared_with: Mapped[int] = mapped_column(ForeignKey("users.uid"), primary_key=True)
    permission: Mapped[Permission] = mapped_column(
        Integer(), default=Permission.VIEW_ONLY
    )
