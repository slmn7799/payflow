from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException

from app.api.dependencies import get_customer_service
from app.api.schemas import CustomerCreate, CustomerList, CustomerOut
from app.domain.errors import NotFoundError
from app.services.customers import CustomerService

router = APIRouter(prefix="/v1/customers", tags=["customers"])

ServiceDep = Annotated[CustomerService, Depends(get_customer_service)]


@router.post("")
def create_customer(body: CustomerCreate, service: ServiceDep) -> CustomerOut:
    customer = service.create(email=body.email, name=body.name)
    return CustomerOut.from_domain(customer)


@router.get("/{customer_id}")
def retrieve_customer(customer_id: str, service: ServiceDep) -> CustomerOut:
    try:
        customer = service.retrieve(customer_id)
    except NotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e)) from e
    return CustomerOut.from_domain(customer)


@router.get("")
def list_customers(service: ServiceDep) -> CustomerList:
    customers = service.list_customers()
    return CustomerList(data=[CustomerOut.from_domain(c) for c in customers])
