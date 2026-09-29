import pytest
from fastapi.testclient import TestClient

from app.main import app, customers

client = TestClient(app)


@pytest.fixture(autouse=True)
def clear_customers():
    customers.clear()
    yield
    customers.clear()


def test_create_customer():
    response = client.post("/v1/customers", json={"email": "a@x.com", "name": "Ann"})

    assert response.status_code == 200
    body = response.json()
    assert body["id"].startswith("cus_")
    assert body["object"] == "customer"
    assert body["email"] == "a@x.com"
    assert body["name"] == "Ann"
    assert isinstance(body["created"], int)


def test_retrieve_missing_customer_returns_404():
    response = client.get("/v1/customers/cus_does_not_exist")

    assert response.status_code == 404


def test_create_then_retrieve_customer():
    created = client.post("/v1/customers", json={"email": "a@x.com"}).json()

    response = client.get(f"/v1/customers/{created['id']}")

    assert response.status_code == 200
    assert response.json() == created


def test_list_customers():
    client.post("/v1/customers", json={"email": "a@x.com"})
    client.post("/v1/customers", json={"email": "b@x.com"})

    response = client.get("/v1/customers")

    assert response.status_code == 200
    body = response.json()
    assert body["object"] == "list"
    assert len(body["data"]) == 2