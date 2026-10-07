from typing import Annotated

from fastapi import Depends

from app.repositories.customers import CustomerRepository, InMemoryCustomerRepository
from app.services.customers import CustomerService

_customer_repo = InMemoryCustomerRepository()


def get_customer_repository() -> CustomerRepository:
    return _customer_repo


def get_customer_service(
    repo: Annotated[CustomerRepository, Depends(get_customer_repository)],
) -> CustomerService:
    return CustomerService(repo)
