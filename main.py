from fastapi import FastAPI
from routers import employees, orders, parts, api_keys
from database import Base, engine

Base.metadata.create_all(bind=engine) 
# reads all your models and creates the tables in the database automatically if they don't exist

app = FastAPI()

app.include_router(parts.router)
app.include_router(orders.router)
app.include_router(employees.router)
app.include_router(api_keys.router)


