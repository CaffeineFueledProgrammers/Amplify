#!/usr/bin/env bash

CLR_GREEN='\033[0;32m'
CLR_RED='\033[0;31m'
CLR_YELLOW='\033[1;33m'
CLR_RESET='\033[0m'

CONFIG_PATH="options.conf"
CWD=${PWD}

# read configuration file
# FRONTEND_HOST=$(grep -Po 'FRONTEND_HOST=\K.*' $CONFIG_PATH)
# FRONTEND_PORT=$(grep -Po 'FRONTEND_PORT=\K.*' $CONFIG_PATH)
BACKEND_HOST=$(grep -Po 'BACKEND_HOST=\K.*' $CONFIG_PATH)
BACKEND_PORT=$(grep -Po 'BACKEND_PORT=\K.*' $CONFIG_PATH)
VENV_PATH=$(grep -Po 'VENV_PATH=\K.*' $CONFIG_PATH)

help_menu() {
    echo "Usage: $0 {frontend|backend} {--dev|--prod}"
    echo
    echo "Commands:"
    echo "  frontend  Start frontend server"
    echo "  backend   Start backend server"
    echo
    echo "Options:"
    echo "  --dev   Run development server"
    echo "  --prod  Run production server"
}

checkFrontendRequirements() {
    echo "Checking frontend requirements..."
    if ! command -v node &>/dev/null; then
        echo -e "${CLR_YELLOW}Node.js${CLR_RESET} is ${CLR_RED}required${CLR_RESET} to run this script."
        exit 1
    fi
    if ! command -v npm &>/dev/null; then
        echo -e "${CLR_YELLOW}NPM${CLR_RESET} is ${CLR_RED}required${CLR_RESET} to run this script."
        exit 1
    fi
    echo "All good!"
}

checkBackendRequirements() {
    echo "Checking backend requirements..."
    if ! command -v python3 &>/dev/null; then
        echo -e "${CLR_YELLOW}Python 3${CLR_RESET} is ${CLR_RED}required${CLR_RESET} to run this script."
        exit 1
    fi
    if ! command -v poetry &>/dev/null; then
        echo -e "${CLR_YELLOW}Poetry${CLR_RESET} is ${CLR_RED}required${CLR_RESET} to run this script."
        exit 1
    fi
    echo "All good!"
}

main() {
    if [ $# -eq 0 ]; then
        help_menu
        exit 1
    fi

    for arg in "$@"; do
        case $arg in
        "frontend")
            CMD_APP="frontend"
            ;;
        "backend")
            CMD_APP="backend"
            ;;
        "--dev")
            CMD_ENV="development"
            ;;
        "--prod")
            CMD_ENV="production"
            ;;
        *)
            help_menu
            exit 1
            ;;
        esac
    done

    if [ -z "$CMD_APP" ] || [ -z "$CMD_ENV" ]; then
        help_menu
        exit 1
    fi

    echo -e "Starting ${CLR_GREEN}${CMD_APP}${CLR_RESET} server in ${CLR_YELLOW}${CMD_ENV}${CLR_RESET} mode..."

    if [ "$CMD_APP" == "frontend" ]; then
        checkFrontendRequirements

        cd amplify_frontend || echo "Directory not found." && exit 1 # change to frontend directory
        npm install                                                  # install dependencies

        echo "Running frontend server..."
        if [ "$CMD_ENV" == "development" ]; then
            echo "npm run dev"
            npm run dev
        elif [ "$CMD_ENV" == "production" ]; then
            echo "npm run build && npm run start"
            npm run build && npm run start
        fi
        cd "${CWD}" || echo "Could not go back to the root directory." && exit 1

    elif [ "$CMD_APP" == "backend" ]; then
        checkBackendRequirements

        # check if already running inside a virtual environment
        if [ -z "$VIRTUAL_ENV" ]; then
            # check if virtual environment exists
            if [ ! -f "${VENV_PATH}/bin/activate" ]; then
                echo "Creating virtual environment..."
                python3 -m venv venv
            fi
            # activate virtual environment
            echo "Activating virtual environment..."
            # shellcheck disable=SC1091
            source "./venv/bin/activate"
        fi

        poetry env info       # show virtual environment information
        poetry install --sync # install dependencies

        echo "Running backend server..."
        if [ "$CMD_ENV" == "development" ]; then
            echo "fastapi dev amplify_backend --host \"$BACKEND_HOST\" --port \"$BACKEND_PORT\" --reload"
            fastapi dev amplify_backend --host "$BACKEND_HOST" --port "$BACKEND_PORT" --reload
        elif [ "$CMD_ENV" == "production" ]; then
            echo "fastapi run amplify_backend --host \"$BACKEND_HOST\" --port \"$BACKEND_PORT\" --no-reload"
            fastapi run amplify_backend --host "$BACKEND_HOST" --port "$BACKEND_PORT" --no-reload
        fi
    fi
}

main "$@"
