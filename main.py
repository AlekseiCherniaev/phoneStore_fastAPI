from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from products.views import router as products_router
from users.views import router as users_router


@asynccontextmanager
async def lifespan(app_: FastAPI):
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(products_router)
app.include_router(users_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", reload=True)
