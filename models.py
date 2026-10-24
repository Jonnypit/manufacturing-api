from sqlalchemy import Column, Integer, String, Float
from database import Base

class Part(Base):
    __tablename__="parts"

    part_id     = Column(Integer, primary_key=True)
    name        = Column(String)
    material    = Column(String)
    quantity    = Column(Integer)
    price       = Column(Float)

class Order(Base):
    __tablename__ = "orders"

    order_id    = Column(Integer, primary_key=True)
    part_id     = Column(Integer)
    quantity    = Column(Integer)
    status      = Column(String)
    date        = Column(String)

class Employee(Base):
    __tablename__ = "employees"

    employee_id  = Column(Integer, primary_key=True)
    name         = Column(String)
    role         = Column(String)
    department   = Column(String)
    hire_date    = Column(String)

