# Dev Environment Management API 🚀

Manage development and staging environments easily via a simple REST API.  
Built with FastAPI, PostgreSQL, Docker, and GitHub Actions CI/CD.

---

## 📋 Features

- Create, Retrieve, Update, Delete (CRUD) Dev Environments
- Extend the duration of an environment
- Fully documented API (Swagger UI, auto-generated)
- PostgreSQL database integration
- Dockerized setup (app + database)
- GitHub Actions CI/CD pipeline (build, lint, security scan)

---

## 🚀 Tech Stack

- Python 3.11
- FastAPI
- PostgreSQL
- SQLAlchemy
- Docker & Docker Compose
- GitHub Actions
- Ruff (linter)
- Trivy (security scan)

---

## 📦 Project Structure

```bash
.
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── database.py
│   ├── schemas.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .dockerignore
├── .env.example
└── .github/
    └── workflows/
        └── ci.yml


## 🏃‍♂️ 🚀 How to Run the Project Locally (Step-by-Step)

Follow these exact commands to run the project locally without Docker:

---

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/dev-env-api.git
cd dev-env-api

## 2. (Optional) Create a Python virtual environment
#(Optional) Create a Python virtual environment
python3 -m venv venv
source venv/bin/activate

### 3. Install Python dependencies
#Install the Python dependencies
pip install --upgrade pip
pip install -r requirements.txt

### 4. Install and start PostgreSQL (if not already installed)
#Install PostgreSQL on Mac (using Homebrew):

brew install postgresql
brew services start postgresql



### 5. Create the database dev_env_db
#Open PostgreSQL shell:

psql -U postgres

#Inside the PostgreSQL prompt, run:

CREATE DATABASE dev_env_db;
\q

✅ Now you have a local database ready!

### 6. Run the FastAPI server

uvicorn app.main:app --reload
✅ If successful, it will print:


Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)

### 7. Access the API documentation
#Open your browser and visit:

http://127.0.0.1:8000/docs — Swagger UI

http://127.0.0.1:8000/redoc — ReDoc UI

✅ You can now create, retrieve, update, and delete Dev Environments!