from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from core import db_helper
from users import crud
from users.crud import validate_user, get_current_token_payload, get_current_active_user
from users.schemas import CreateUser, Token
from auth.utils import encode_jwt
from .schemas import User

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.post("/add-user/")
async def create_user(
    user: CreateUser,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> User:
    return await crud.create_user(user_in=user, session=session)


@router.get("/user/")
async def get_user(
    username: str,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> User:
    if user := await crud.get_user_by_username(session=session, username=username):
        return user
    else:
        raise HTTPException(status_code=404, detail="User not found")


@router.post("/login/")
async def auth_user_issue_jwt(
    user: User = Depends(validate_user),
) -> Token:
    jwt_payload = {
        "sub": user.username,
        "username": user.username,
        "email": user.email,
    }
    token = encode_jwt(jwt_payload)
    return Token(
        access_token=token,
        token_type="Bearer",
    )


@router.get("/me/")
async def auth_user_check_self_info(
    payload: dict = Depends(get_current_token_payload),
    user: User = Depends(get_current_active_user),
) -> dict:
    iat = payload.get("iat")
    return {
        "username": user.username,
        "email": user.email,
        "logged_in_at": iat,
    }


@router.post("/registration/")
async def register_user(
    user: User = Depends(create_user),
) -> Token:
    jwt_payload = {
        "sub": user.username,
        "username": user.username,
        "email": user.email,
    }
    token = encode_jwt(jwt_payload)
    return Token(
        access_token=token,
        token_type="Bearer",
    )


@router.delete("/delete-user/")
async def delete_user(
    username: str, session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> None:
    return await crud.delete_user(username=username, session=session)
