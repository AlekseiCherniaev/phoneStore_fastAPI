from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import db_helper
from . import crud
from .schemas import Phone, ProductCreate

router = APIRouter(
    prefix="/phones",
    tags=["phones"],
)


@router.get("/")
async def get_phones(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> list[Phone]:
    return await crud.get_products(session=session)


@router.post("/add-phone/")
async def add_phone(
    product_in: ProductCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Phone:
    return await crud.create_products(session=session, product_in=product_in)


@router.get("/{phone_id}/")
async def get_phone(
    phone_id: int, session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> Phone:
    product = await crud.get_product_by_id(session=session, id_=phone_id)
    if product:
        return product
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Product_id not found"
        )
