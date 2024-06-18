"""
Amplify - AI-Powered Note-Taking for Students
"""

NAME: str = "Amplify"
VERSION: tuple[int, ...] = (0, 0, 1)
TITLE: str = f"{NAME} v{'.'.join(map(str, VERSION))}"

DATABASE_URL: str = "sqlite:///./data/amplify.db"
