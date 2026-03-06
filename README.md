# HRMS Lite Backend (FastAPI + PostgreSQL)

## Features
- Employee CRUD APIs
- Attendance management
- PostgreSQL (Neon) database
- FastAPI with SQLAlchemy

## Run Locally

1. Create virtual environment
2. Install dependencies

pip install -r requirements.txt

3. Set environment variable in .env

DATABASE_URL=postgresql://neondb_owner:npg_ifdQ5YzDrn6W@ep-morning-violet-aeca0plp-pooler.c-2.us-east-2.aws.neon.tech/neondb?sslmode=require&channel_binding=require

4. Run server

uvicorn main:app --reload

API docs:
http://127.0.0.1:8000/docs
