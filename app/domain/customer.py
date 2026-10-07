import secrets
import time
from dataclasses import dataclass


@dataclass(frozen=True)
class Customer:
    id: str
    created: int
    email: str | None
    name: str | None

    @staticmethod
    def new(email: str | None, name: str | None) -> "Customer":
        return Customer(
            id="cus_" + secrets.token_hex(8),
            created=int(time.time()),
            email=email,
            name=name,
        )
