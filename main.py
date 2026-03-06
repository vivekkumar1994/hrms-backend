from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine
from app.employee_routes import router as employee_router
from app.attendance_routes import router as attendance_router

app = FastAPI(title="HRMS Lite API")

# Create tables
Base.metadata.create_all(bind=engine)

# Allowed frontend domains
origins = [
    "http://localhost:3000",  # local development
    "https://hrms-frontend-omega-woad.vercel.app",  # live frontend
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(employee_router)
app.include_router(attendance_router)


@app.get("/")
def root():
    return {"message": "HRMS Backend Running"}