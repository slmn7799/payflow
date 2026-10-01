import secrets
import time
from typing import Any

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="PayFlow")

customers: dict[str, dict[str, Any]] = {}


class CustomerCreate(BaseModel):
    email: str | None = None
    name: str | None = None


@app.get("/")
def home() -> dict[str, str]:
    return {"message": "Hello from PayFlow"}


@app.post("/v1/customers")
def create_customer(body: CustomerCreate) -> dict[str, Any]:
    customer_id = "cus_" + secrets.token_hex(8)
    customer = {
        "id": customer_id,
        "object": "customer",
        "created": int(time.time()),
        "email": body.email,
        "name": body.name,
    }
    customers[customer_id] = customer
    return customer


@app.get("/v1/customers/{customer_id}")
def retrieve_customer(customer_id: str) -> dict[str, Any]:
    if customer_id not in customers:
        raise HTTPException(status_code=404, detail=f"No such customer: '{customer_id}'")
    return customers[customer_id]


@app.get("/v1/customers")
def list_customers() -> dict[str, Any]:
    list_of_customers = {"object": "list", "data": list(customers.values())}
    return list_of_customers
