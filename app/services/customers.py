from app.domain.customer import Customer
from app.domain.errors import NotFoundError
from app.repositories.customers import CustomerRepository


class CustomerService:
    def __init__(self, repo: CustomerRepository) -> None:
        self._repo = repo

    def create(self, email: str | None, name: str | None) -> Customer:
        customer = Customer.new(email=email, name=name)
        self._repo.add(customer)
        return customer

    def retrieve(self, customer_id: str) -> Customer:
        customer = self._repo.get(customer_id)
        if customer is None:
            raise NotFoundError("customer", customer_id)
        return customer

    def list_customers(self) -> list[Customer]:
        return self._repo.list_all()
