from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import SessionLocal
from .models import Attendance, Employee
from .schemas import AttendanceCreate

router = APIRouter(
    prefix="/attendance",
    tags=["Attendance"]
)


# Database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# -----------------------------
# Mark Attendance
# -----------------------------
@router.post("/")
def mark_attendance(data: AttendanceCreate, db: Session = Depends(get_db)):

    # Check employee exists
    emp = db.query(Employee).filter(
        Employee.employeeId == data.employeeId
    ).first()

    if not emp:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    # Prevent duplicate attendance on same date
    existing = db.query(Attendance).filter(
        Attendance.employeeId == data.employeeId,
        Attendance.date == data.date
    ).first()

    if existing:
        raise HTTPException(
            status_code=409,
            detail="Attendance already marked for this date"
        )

    attendance = Attendance(**data.dict())

    db.add(attendance)
    db.commit()

    return {"message": "Attendance marked successfully"}


# -----------------------------
# Get All Attendance
# -----------------------------
@router.get("/")
def get_all_attendance(db: Session = Depends(get_db)):

    records = db.query(Attendance).all()

    return records


# -----------------------------
# Get Attendance By Employee
# -----------------------------
@router.get("/{employeeId}")
def get_attendance(employeeId: str, db: Session = Depends(get_db)):

    records = db.query(Attendance).filter(
        Attendance.employeeId == employeeId
    ).all()

    if not records:
        raise HTTPException(
            status_code=404,
            detail="No attendance records found"
        )

    return records