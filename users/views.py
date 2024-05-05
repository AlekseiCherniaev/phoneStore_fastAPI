from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession
from passlib.context import CryptContext
from core.models import db_helper
from users import crud
from users.schemas import CreateUser
from core.config import settings
from auth.utils import validate_password

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.post("/")
async def create_user(
    user: CreateUser,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_user(user_in=user, session=session)


@router.get("/user/")
async def get_user(
    username: str,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    if user := await crud.get_user(session=session, username=username):
        return user
    else:
        raise HTTPException(status_code=404, detail="User not found")
