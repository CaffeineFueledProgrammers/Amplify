"""
Amplify - AI-Powered Note-Taking for Students
"""

import argparse

from amplify_backend import config
from amplify_backend.routes import get_app


def main():
    """
    The main function of the application.
    """

    argparser = argparse.ArgumentParser(
        description="Amplify - AI-Powered Note-Taking for Students"
    )
    _ = argparser.add_argument(
        "mode",
        choices=["dev", "test", "prod"],
        help="The mode to run the application in",
    )

    args = argparser.parse_args()
    print(f"Running in {args.mode} mode")  # pyright: ignore[reportAny]

    match args.mode:  # pyright: ignore[reportAny]
        case "dev":
            mode_config = config.DevConfig

        case "test":
            mode_config = config.TestConfig

        case "prod":
            mode_config = config.ProdConfig

        case _:  # pyright: ignore[reportAny]
            raise ValueError(f"Invalid mode: {args.mode}")  # pyright: ignore[reportAny]

    flask_app = get_app()
    flask_app.run(host=mode_config.HOST, port=mode_config.PORT, debug=mode_config.DEBUG)


if __name__ == "__main__":
    main()
