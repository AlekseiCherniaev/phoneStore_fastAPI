from typing import Annotated

from fastapi import Path, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core import db_helper
from core.exceptions import ProductNotFoundException
from core.models import Product
from . import crud


async def product_by_id(
    product_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Product:
    product = await crud.get_product_by_id(session=session, product_id=product_id)
    if product is not None:
        return product
    else:
        raise ProductNotFoundException
