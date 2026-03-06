from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine
from app.employee_routes import router as employee_router
from app.attendance_routes import router as attendance_router


app = FastAPI(title="HRMS Lite API")

# Create tables
Base.metadata.create_all(bind=engine)

# CORS configuration
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "https://hrms-frontend-omega-woad.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Frontend URLs
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