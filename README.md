# Manufacturing API

A REST API built with FastAPI and SQLite demonstrating full CRUD operations across three manufacturing resources — parts, orders, and employees.

## Tech Stack

- **FastAPI** — web framework
- **SQLAlchemy** — database ORM
- **SQLite** — database
- **Pydantic** — data validation
- **Uvicorn** — ASGI server

## Project Structure

```
manufacturing-api/
├── main.py              # app entry point, router assembly
├── database.py          # SQLite connection and session setup
├── models.py            # SQLAlchemy table definitions
├── dependencies.py      # database session dependency
├── requirements.txt     # project dependencies
└── routers/
    ├── parts.py         # parts endpoints
    ├── orders.py        # orders endpoints
    └── employees.py     # employees endpoints
```

## Endpoints

### Parts
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/parts` | Get all parts |
| GET | `/parts/{part_id}` | Get part by ID |
| POST | `/parts` | Create a new part |
| PUT | `/parts/{part_id}` | Update a part |
| DELETE | `/parts/{part_id}` | Delete a part |

### Orders
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/orders` | Get all orders |
| GET | `/orders/{order_id}` | Get order by ID |
| POST | `/orders` | Create a new order |
| PUT | `/orders/{order_id}` | Update an order |
| DELETE | `/orders/{order_id}` | Delete an order |

### Employees
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/employees` | Get all employees |
| GET | `/employees/{employee_id}` | Get employee by ID |
| POST | `/employees` | Create a new employee |
| PUT | `/employees/{employee_id}` | Update an employee |
| DELETE | `/employees/{employee_id}` | Delete an employee |

## Getting Started

**1. Clone the repository**
```bash
git clone https://github.com/Jonnypit/manufacturing-api.git
cd manufacturing-api
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Configure environment variables**

Create a `.env` file in the project root:
```
DATABASE_URL=sqlite:///./manufacturing.db
```

**4. Run the server**
```bash
uvicorn main:app --reload
```

**4. Open the interactive docs**
```
http://localhost:8000/docs
```

The SQLite database is created automatically on first run.

## Key Concepts Demonstrated

- REST API design with FastAPI
- SQLAlchemy ORM for database operations
- Pydantic models for request body validation
- Dependency injection for database session management
- Modular router architecture — one file per resource
- HTTP status codes and error handling with HTTPException
