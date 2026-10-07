from typing import Literal

from pydantic import BaseModel

from app.domain.customer import Customer


class CustomerCreate(BaseModel):
    email: str | None = None
    name: str | None = None


class CustomerOut(BaseModel):
    id: str
    object: Literal["customer"] = "customer"
    created: int
    email: str | None
    name: str | None

    @classmethod
    def from_domain(cls, customer: Customer) -> "CustomerOut":
        return cls(
            id=customer.id, created=customer.created, email=customer.email, name=customer.name
        )


class CustomerList(BaseModel):
    object: Literal["list"] = "list"
    data: list[CustomerOut]
