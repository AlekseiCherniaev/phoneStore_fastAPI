from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result

from core.exceptions import ProductAlreadyExistsException
from products.schemas import ProductCreate, ProductUpdate, ProductUpdatePartial
from core.models import Product


async def get_products(session: AsyncSession) -> list[Product]:
    statement = select(Product).order_by(Product.id)
    result: Result = await session.execute(statement)
    products = result.scalars().all()
    return list(products)


async def get_product_by_id(session: AsyncSession, product_id: int) -> Product | None:
    return await session.get(Product, product_id)


async def create_products(session: AsyncSession, product_in: ProductCreate) -> Product:
    statement = select(Product).where(Product.name == product_in.name)
    result: Result = await session.execute(statement)
    product_ = result.scalar_one_or_none()
    if not product_:
        product = Product(**product_in.model_dump())
        session.add(product)
        await session.commit()
        # await session.refresh(product)
        return product
    else:
        raise ProductAlreadyExistsException


async def update_product(
    session: AsyncSession,
    product: Product,
    product_update: ProductUpdate | ProductUpdatePartial,
    partial: bool = False,
) -> Product:
    statement = select(Product).where(Product.name == product_update.name)
    result: Result = await session.execute(statement)
    product_ = result.scalar_one_or_none()
    if not product_ or product_.name == product_update.name:
        for key, value in product_update.model_dump(exclude_unset=partial).items():
            setattr(product, key, value)
        await session.commit()
        return product
    else:
        raise ProductAlreadyExistsException


async def delete_product(
    session: AsyncSession,
    product: Product,
) -> None:
    await session.delete(product)
    await session.commit()
