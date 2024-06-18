"""
Amplify - AI-Powered Note-Taking for Students
"""

# pylint: disable=R0903

from sqlalchemy import Boolean, Text
from sqlalchemy.orm import Mapped, mapped_column

from amplify_backend.models.base import Base


class Note(Base):
    """This class represents a user's note.

    Attributes:
        uid: The unique identifier of the note.
        version: The spec version of the note.
        content: The content of the note.
        is_public: Whether the note is publicly accessible or not.
    """

    __tablename__: str = "notes"

    uid: Mapped[int] = mapped_column(primary_key=True)
    version: Mapped[int] = mapped_column()
    content: Mapped[str] = mapped_column(Text())
    is_public: Mapped[bool] = mapped_column(Boolean())
