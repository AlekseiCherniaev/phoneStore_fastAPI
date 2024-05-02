from contextlib import asynccontextmanager

from fastapi import FastAPI
from products.views import router as products_router
from users.views import router as users_router


@asynccontextmanager
async def lifespan(app_: FastAPI):
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(products_router)
app.include_router(users_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
