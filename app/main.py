from fastapi import FastAPI

from app.api import customers

app = FastAPI(title="PayFlow")
app.include_router(customers.router)


@app.get("/")
def home() -> dict[str, str]:
    return {"message": "Hello from PayFlow"}
