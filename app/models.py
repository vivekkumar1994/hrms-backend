from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    employeeId = Column(String, unique=True, index=True)
    fullName = Column(String)
    email = Column(String, unique=True)
    department = Column(String)

    attendance = relationship("Attendance", back_populates="employee", cascade="all, delete")


class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, index=True)
    employeeId = Column(String, ForeignKey("employees.employeeId"))
    date = Column(Date)
    status = Column(String)

    employee = relationship("Employee", back_populates="attendance")