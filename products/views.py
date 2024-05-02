from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import db_helper
from . import crud
from .schemas import Product, ProductCreate, ProductUpdate
from products.dependencies import product_by_id

router = APIRouter(
    prefix="/phones",
    tags=["phones"],
)


@router.get("/")
async def get_products(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> list[Product]:
    return await crud.get_products(session=session)


@router.post("/add-product/")
async def add_phone(
    product_in: ProductCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Product:
    return await crud.create_products(session=session, product_in=product_in)


@router.get("/{product_id}/")
async def get_phone(phone: Product = Depends(product_by_id)) -> Product:
    return phone


@router.delete("/{product_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_phone(
    phone: Product = Depends(product_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> None:
    await crud.delete_product(session=session, product=phone)


@router.put("/{product_id}/")
async def update_product(
    phone_update: ProductUpdate,
    phone: Product = Depends(product_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Product:
    return await crud.update_product(
        session=session, product=phone, product_update=phone_update
    )


@router.patch("/{product_id}/")
async def patch_product(
    phone_update: ProductUpdate,
    phone: Product = Depends(product_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Product:
    return await crud.update_product(
        session=session, product=phone, product_update=phone_update, partial=True
    )
