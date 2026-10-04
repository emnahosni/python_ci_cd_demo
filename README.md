# Python CI/CD Demo

A small Flask REST API created as a hands-on project to practice a real-world software development workflow.

## Project Goal

This project is designed to consolidate practical skills in:

* Python REST API development
* Git and GitHub
* Docker
* Automated testing
* CI/CD with GitHub Actions

## Tech Stack

* Python 3.10
* Flask
* Git / GitHub
* Docker
* GitHub Actions

## API

### Health Check

**GET** `/health`

Returns:

```json
{
  "status": "ok"
}
```

## Run Locally

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

The API will be available at:

`http://127.0.0.1:5000/health`

## Project Status

Currently implemented:

* Flask REST API
* Health check endpoint
* Python virtual environment
* Git version control
* GitHub repository

Upcoming:

* Automated tests
* Docker containerization
* GitHub Actions CI/CD
* Simulated feature development using branches and pull requests
