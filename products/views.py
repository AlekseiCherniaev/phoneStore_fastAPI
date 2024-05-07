from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from core import db_helper
from . import crud
from .schemas import Product, ProductCreate, ProductUpdate, ProductUpdatePartial
from products.dependencies import product_by_id

router = APIRouter(
    prefix="/products",
    tags=["products"],
)


@router.get("/all-products/")
async def get_products(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> list:
    return await crud.get_products(session=session)


@router.post("/add-product/")
async def add_product(
    product_in: ProductCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Product:
    return await crud.create_products(session=session, product_in=product_in)


@router.get("/{product_id}/")
async def get_product(product: Product = Depends(product_by_id)) -> Product:
    return product


@router.delete("/{product_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(
    product: Product = Depends(product_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> None:
    await crud.delete_product(session=session, product=product)


@router.put("/{product_id}/")
async def update_product(
    product_update: ProductUpdate,
    product: Product = Depends(product_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Product:
    return await crud.update_product(
        session=session, product=product, product_update=product_update
    )


@router.patch("/{product_id}/")
async def patch_product(
    phone_update: ProductUpdatePartial,
    phone: Product = Depends(product_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Product:
    return await crud.update_product(
        session=session, product=phone, product_update=phone_update, partial=True
    )
