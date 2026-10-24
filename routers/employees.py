from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies import get_db
from models import Employee
from pydantic import BaseModel

class EmployeeCreate(BaseModel):
    name: str
    role: str
    department: str
    hire_date: str

router = APIRouter()

@router.get("/employees")
def get_employees(db: Session = Depends(get_db)):
    employees = db.query(Employee).all()
    return employees

@router.get("/employees/{employee_id}")
def get_employees(employee_id: int, db: Session = Depends(get_db)):
    employee = db.query(Employee).filter(Employee.employee_id == employee_id).first()
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

@router.post("/employees")
def create_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
    new_employee = Employee(
        name=employee.name,
        role=employee.role,
        department=employee.department,
        hire_date=employee.hire_date
    )
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)
    return new_employee

@router.put("/employees/{employee_id}")
def update_employee(employee_id: int, employee: EmployeeCreate, db: Session = Depends(get_db)):
    existing_employee = db.query(Employee).filter.Employee.empolyee_id == employee_id.first()
    if existing_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    existing_employee.name      = employee.name
    existing_employee.role          = employee.role
    existing_employee.department    = employee.department
    existing_employee.hire_date     = employee.hire_date
    db.commit()
    db.refresh(existing_employee)
    return existing_employee

@router.delete("/employees/{employee_id}")
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    employee = db.query(Employee).filter(employee.employee_id == employee_id).first()
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    db.delete(employee)
    db.commit()
    return {"message": f"Employee { employee_id} deleted"}

