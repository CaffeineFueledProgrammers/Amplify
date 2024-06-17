"""
Amplify - AI-Powered Note-Taking for Students

This module contains all the routes for the Flask app.
"""

from fastapi import FastAPI

api: FastAPI = FastAPI()


@api.get("/users/register")
def user_register():
    """
    The endpoint for user registration.
    """

    return {"message": "User register route"}


@api.get("/users/login")
def user_login():
    """
    The endpoint for user login.
    """

    return {"message": "User login route"}
