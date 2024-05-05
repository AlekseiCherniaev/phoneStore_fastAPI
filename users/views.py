from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession
from passlib.context import CryptContext

from core.models import db_helper, User
from users import crud
from users.crud import validate_user
from users.schemas import SCreateUser, SToken, SUserLogin
from core.config import settings
from auth.utils import validate_password, encode_jwt

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.post("/")
async def create_user(
    user: SCreateUser,
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


@router.post("/login/")
async def auth_user_issue_jwt(
    user: User = Depends(validate_user),
) -> SToken:
    jwt_payload = {
        "sub": user.username,
        "username": user.username,
        "email": user.email,
    }
    token = encode_jwt(jwt_payload)
    return SToken(
        access_token=token,
        token_type="Bearer",
    )


# @router.get("/users/me/")
# def auth_user_check_self_info(
#     payload: dict = Depends(get_current_token_payload),
#     user: UserLogin = Depends(get_current_active_auth_user),
# ) -> dict:
#     iat = payload.get("iat")
#     return {
#         "username": user.username,
#         "email": user.email,
#         "logged_in_at": iat,
#     }
