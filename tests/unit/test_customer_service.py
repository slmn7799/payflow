import pytest

from app.domain.errors import NotFoundError
from app.repositories.customers import InMemoryCustomerRepository
from app.services.customers import CustomerService


def make_service() -> CustomerService:
    return CustomerService(InMemoryCustomerRepository())


def test_create_then_retrieve() -> None:
    service = make_service()

    created = service.create(email="a@x.com", name="Ann")

    assert created.id.startswith("cus_")
    assert service.retrieve(created.id) == created


def test_retrieve_missing_raises_not_found() -> None:
    service = make_service()

    with pytest.raises(NotFoundError):
        service.retrieve("cus_nope")
