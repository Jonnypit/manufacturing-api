from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_parts():
    response = client .get("/orders")
    assert response.status_code == 200

def test_create_order():
    response = client.post("/orders", json={
        "part_id": 42,
        "quantity": 100,
        "status": "pending",
        "date": "2026-10-25"
    })
    assert response.status_code == 200
    assert response.json()["part_id"] 

def test_get_order_not_found():
    response = client.get("/orders/999")
    assert response.status_code == 404

def test_create_order_invalid():
    response = client.post("/parts", json={
        "part_id": 42,
        "quantity": 100,
        "status": 42,
        "date": "2026-10-25"
        })
    assert response.status_code == 422