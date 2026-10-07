from typing import Protocol

from app.domain.customer import Customer


class CustomerRepository(Protocol):
    def add(self, customer: Customer) -> None: ...
    def get(self, customer_id: str) -> Customer | None: ...
    def list_all(self) -> list[Customer]: ...


class InMemoryCustomerRepository:
    def __init__(self) -> None:
        self._items: dict[str, Customer] = {}

    def add(self, customer: Customer) -> None:
        self._items[customer.id] = customer

    def get(self, customer_id: str) -> Customer | None:
        return self._items.get(customer_id)

    def list_all(self) -> list[Customer]:
        return list(self._items.values())
