"""
Amplify - AI-Powered Note-Taking for Students
"""

# pylint: disable=R0903

from sqlalchemy import Boolean, String
from sqlalchemy.orm import Mapped, mapped_column

from amplify_backend.models.base import Base


class User(Base):
    """This class represents a user.

    Attributes:
        uid: The unique identifier of the user.
        username: The chosen username of the user.
        password: The hashed password of the user.
        salt: The salt used to hash the password.
        first_name: The first name of the user.
        last_name: The last name of the user.
        is_admin: A boolean indicating if the user is an administrator.
    """

    __tablename__: str = "users"

    uid: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(25))
    password: Mapped[str] = mapped_column(String(64))
    salt: Mapped[str] = mapped_column(String(32))

    first_name: Mapped[str | None] = mapped_column(String(40))
    last_name: Mapped[str | None] = mapped_column(String(40))
    is_admin: Mapped[bool] = mapped_column(Boolean())
