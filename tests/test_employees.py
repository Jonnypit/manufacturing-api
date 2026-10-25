from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_employee():
    response = client.get("/employees")
    assert response.status_code == 200

def test_create_employee():
    response = client.post("/employees", json={
        "name": "Jon",
        "role": "CEO",
        "department": "admin",
        "hire_date": "2026-10-26"
    })
    assert response.status_code == 200
    assert response.json()["name"] == "Jon"

def test_get_employee_not_found():
    response = client.get("/emoployee/bill")
    assert response.status_code == 404

def test_create_employee_invalid():
    response = client.post("/employees", json={
        "name": 42,
        "role": "CEO",
        "department": "admin",
        "hire_date": "2026-10-26"
    })
    assert response.status_code == 422



