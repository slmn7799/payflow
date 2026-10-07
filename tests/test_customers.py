from collections.abc import Iterator

import pytest
from fastapi.testclient import TestClient

from app.api.dependencies import get_customer_repository
from app.main import app
from app.repositories.customers import InMemoryCustomerRepository

client = TestClient(app)


@pytest.fixture(autouse=True)
def fresh_repository() -> Iterator[None]:
    repo = InMemoryCustomerRepository()
    app.dependency_overrides[get_customer_repository] = lambda: repo
    yield
    app.dependency_overrides.clear()


def test_create_customer() -> None:
    response = client.post("/v1/customers", json={"email": "a@x.com", "name": "Ann"})

    assert response.status_code == 200
    body = response.json()
    assert body["id"].startswith("cus_")
    assert body["object"] == "customer"
    assert body["email"] == "a@x.com"
    assert body["name"] == "Ann"
    assert isinstance(body["created"], int)


def test_retrieve_missing_customer_returns_404() -> None:
    response = client.get("/v1/customers/cus_does_not_exist")

    assert response.status_code == 404


def test_create_then_retrieve_customer() -> None:
    created = client.post("/v1/customers", json={"email": "a@x.com"}).json()

    response = client.get(f"/v1/customers/{created['id']}")

    assert response.status_code == 200
    assert response.json() == created


def test_list_customers() -> None:
    client.post("/v1/customers", json={"email": "a@x.com"})
    client.post("/v1/customers", json={"email": "b@x.com"})

    response = client.get("/v1/customers")

    assert response.status_code == 200
    body = response.json()
    assert body["object"] == "list"
    assert len(body["data"]) == 2
