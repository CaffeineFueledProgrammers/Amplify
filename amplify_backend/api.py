"""
Amplify - AI-Powered Note-Taking for Students

This contains the API endpoints.
"""

# pyright: reportCallInDefaultInitializer=false

import random

from fastapi import Body, Depends, FastAPI, HTTPException, Request, status
from fastapi.security import HTTPBasicCredentials
from sqlalchemy import select
from sqlalchemy.orm import Session

from amplify_backend import database
from amplify_backend.models.user import User

api: FastAPI = FastAPI()

# In-memory session storage (for testing purposes)
sessions: dict[int, int] = {}  # <session_id, user_id>


def authenticate_user(credentials: HTTPBasicCredentials):
    """
    Authenticates the user based on the provided credentials.
    """

    user = users.get(credentials.username)
    if user is None or user.password != credentials.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Basic"},
        )
    return user


def create_session(user_id: int) -> int:
    """
    Creates a new session for the user.
    """

    session_id = len(sessions) + random.randint(0, 1000000)
    sessions[session_id] = user_id
    return session_id


def get_user_from_session(request: Request):
    """
    Gets the user from the session.
    """

    session_id = request.cookies.get("session_id")
    if session_id is None or int(session_id) not in sessions:
        raise HTTPException(
            status_code=401,
            detail="Invalid session ID",
        )
    return sessions[int(session_id)]


@api.post("/register")
def user_register(username: str = Body(), password: str = Body()):
    """
    The endpoint for user registration.
    """

    with Session(database.get_db_engine()) as db_session:
        # check if the username is already taken
        if select(User).where(User.username == username):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT, detail="Username already taken"
            )

        # new_user = User(
        #     uid=len(users) + 1,
        #     username=username,
        #     password=password,
        # )
        new_user = User(
            uid=len(users) + 1,
            username=username,
            password=password,
        )
        users[new_user.username] = new_user
        return {"message": "User registered successfully"}


@api.post("/login")
def user_login(user: User = Depends(authenticate_user)):
    """
    The endpoint for user login.
    """

    session_id = create_session(user.uid)
    return {"message": "Logged in successfully", "session_id": session_id}


# TODO: Remove these development endpoints before deployment


@api.get("/dev/users")
def get_users(user_id: int = Depends(get_user_from_session)):
    """
    A temporary development endpoint to get all registered users.
    """

    return (user_id, users)


@api.get("/dev/sessions")
def get_sessions(user_id: int = Depends(get_user_from_session)):
    """
    A temporary development endpoint to get all sessions.
    """

    return (user_id, sessions)
