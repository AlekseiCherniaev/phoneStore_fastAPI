from contextlib import asynccontextmanager

from fastapi import FastAPI

from core.models import db_helper, Base
from products.views import router as products_router


@asynccontextmanager
async def lifespan(app_: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield


app = FastAPI(lifespan=lifespan)
app.include_router(products_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
