from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result
from products.schemas import Phone, ProductCreate
from core import models


async def get_products(session: AsyncSession) -> list[models.Phone]:
    statement = select(models.Phone).order_by(models.Phone.id)
    result: Result = await session.execute(statement)
    products = result.scalars().all()
    return list(products)


async def get_product_by_id(session: AsyncSession, id_: int) -> models.Phone | None:
    return await session.get(models.Phone, id_)


async def create_products(session: AsyncSession, product_in: ProductCreate) -> models.Phone:
    product = models.Phone(**product_in.model_dump())
    session.add(product)
    await session.commit()
    # await session.refresh(product)
    return product
