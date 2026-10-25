from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_parts():
    repsonse = client.get("/parts")
    assert repsonse.status_code == 200

def test_create_part():
    response = client.post("/parts", json={
        "name": "bolt",
        "material": "steel",
        "quantity": 100,
        "price": 0.25
    })
    assert response.status_code == 200
    assert response.json()["name"] == "bolt"

def test_get_part_not_found():
    response = client.get("/parts/999")
    assert response.status_code == 404

def test_create_part_invalid():
    response = client.post("/parts", json={
        "name": "bolt",
        "material": "steel",
        "quantity": "not a number",
        "price": 0.25
        })
    assert response.status_code == 422
