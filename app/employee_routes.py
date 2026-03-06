from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import SessionLocal
from .models import Employee
from .schemas import EmployeeCreate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/employees")
def create_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):

    existing = db.query(Employee).filter(Employee.employeeId == employee.employeeId).first()

    if existing:
        raise HTTPException(status_code=409, detail="Employee already exists")

    new_emp = Employee(**employee.dict())

    db.add(new_emp)
    db.commit()

    return {"message": "Employee created"}

@router.get("/employees")
def get_employees(db: Session = Depends(get_db)):

    employees = db.query(Employee).all()

    return employees

@router.delete("/employees/{employeeId}")
def delete_employee(employeeId: str, db: Session = Depends(get_db)):

    emp = db.query(Employee).filter(Employee.employeeId == employeeId).first()

    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")

    db.delete(emp)
    db.commit()

    return {"message": "Employee deleted"}
