$CLR_GREEN = [System.ConsoleColor]::Green
$CLR_RED = [System.ConsoleColor]::Red
$CLR_YELLOW = [System.ConsoleColor]::Yellow
$CLR_RESET = [System.ConsoleColor]::White

$CONFIG_PATH = "options.conf"
$CWD = Get-Location

# read configuration file
$BACKEND_HOST = (Select-String -Path $CONFIG_PATH -Pattern 'BACKEND_HOST=(.*)').Matches.Groups[1].Value
$BACKEND_PORT = (Select-String -Path $CONFIG_PATH -Pattern 'BACKEND_PORT=(.*)').Matches.Groups[1].Value
$VENV_PATH = (Select-String -Path $CONFIG_PATH -Pattern 'VENV_PATH=(.*)').Matches.Groups[1].Value

function help_menu {
    Write-Host "Usage: $0 {frontend|backend} {--dev|--prod}"
    Write-Host ""
    Write-Host "Commands:"
    Write-Host "  frontend  Start frontend server"
    Write-Host "  backend   Start backend server"
    Write-Host ""
    Write-Host "Options:"
    Write-Host "  --dev   Run development server"
    Write-Host "  --prod  Run production server"
}

function checkFrontendRequirements {
    Write-Host "Checking frontend requirements..."
    if (!(Get-Command node -ErrorAction SilentlyContinue)) {
        Write-Host "Node.js is required to run this script." -ForegroundColor $CLR_YELLOW
        exit
    }
    if (!(Get-Command npm -ErrorAction SilentlyContinue)) {
        Write-Host "NPM is required to run this script." -ForegroundColor $CLR_YELLOW
        exit
    }
    Write-Host "All good!"
}

function checkBackendRequirements {
    Write-Host "Checking backend requirements..."
    if (!(Get-Command python3 -ErrorAction SilentlyContinue)) {
        Write-Host "Python 3 is required to run this script." -ForegroundColor $CLR_YELLOW
        exit
    }
    if (!(Get-Command poetry -ErrorAction SilentlyContinue)) {
        Write-Host "Poetry is required to run this script." -ForegroundColor $CLR_YELLOW
        exit
    }
    Write-Host "All good!"
}

function main {
    if ($args.Length -eq 0) {
        help_menu
        exit
    }

    $CMD_APP = $null
    $CMD_ENV = $null

    foreach ($arg in $args) {
        switch ($arg) {
            "frontend" { $CMD_APP = "frontend" }
            "backend" { $CMD_APP = "backend" }
            "--dev" { $CMD_ENV = "development" }
            "--prod" { $CMD_ENV = "production" }
            default {
                help_menu
                exit
            }
        }
    }

    if ($null -eq $CMD_APP -or $null -eq $CMD_ENV) {
        help_menu
        exit
    }

    Write-Host "Starting $CMD_APP server in $CMD_ENV mode..." -ForegroundColor $CLR_GREEN

    if ($CMD_APP -eq "frontend") {
        checkFrontendRequirements

        Set-Location amplify_frontend # change to frontend directory
        npm install # install dependencies

        Write-Host "Running frontend server..."
        if ($CMD_ENV -eq "development") {
            npm run dev
        }
        elseif ($CMD_ENV -eq "production") {
            npm run build
            npm run start
        }
        Set-Location $CWD
    }
    elseif ($CMD_APP -eq "backend") {
        checkBackendRequirements

        # check if already running inside a virtual environment
        if ($null -eq $env:VIRTUAL_ENV) {
            # check if virtual environment exists
            if (!(Test-Path "${VENV_PATH}\Scripts\Activate.ps1")) {
                Write-Host "Creating virtual environment..."
                python3 -m venv venv
            }
            # activate virtual environment
            Write-Host "Activating virtual environment..."
            Invoke-Expression "${VENV_PATH}\Scripts\Activate.ps1"
        }

        poetry env info # show virtual environment information
        poetry install --sync # install dependencies

        Write-Host "Running backend server..."
        if ($CMD_ENV -eq "development") {
            fastapi dev amplify_backend --host "$BACKEND_HOST" --port "$BACKEND_PORT" --reload
        }
        elseif ($CMD_ENV -eq "production") {
            fastapi run amplify_backend --host "$BACKEND_HOST" --port "$BACKEND_PORT" --no-reload
        }
    }
}

main $args
