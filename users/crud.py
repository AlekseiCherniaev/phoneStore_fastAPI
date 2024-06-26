from fastapi import Depends, Form
from fastapi.security import OAuth2PasswordBearer
from jwt import InvalidTokenError
from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import AsyncSession


from auth import utils
from auth.utils import validate_password, decode_jwt, password_check_complexity
from core.exceptions import (
    UserAlreadyExistsException,
    PasswordNotValidException,
    UserNotFoundException,
    WrongPasswordException,
    InvalidTokenException,
    UserInactiveException,
)
from core.models import User
from core import db_helper
from users.schemas import CreateUser

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/users/login/",
)


async def get_user_by_username(session: AsyncSession, username: str) -> User | None:
    statement = select(User).where(User.username == username)
    result: Result = await session.execute(statement)
    user = result.scalar_one_or_none()
    return user


async def create_user(user_in: CreateUser, session: AsyncSession) -> User:
    user = await get_user_by_username(session, user_in.username)
    if not user:
        user_data = user_in.model_dump()
        if not password_check_complexity(user_data["password"]):
            raise PasswordNotValidException
        user_data["password"] = utils.hash_password(user_data["password"])
        user = User(**user_data)
        session.add(user)
        await session.commit()
        return user
    else:
        raise UserAlreadyExistsException


async def delete_user(username: str, session: AsyncSession) -> None:
    user = await get_user_by_username(session, username)
    if user:
        await session.delete(user)
        await session.commit()
    else:
        raise UserNotFoundException


async def validate_user(
    username: str = Form(),
    password: str = Form(),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> User:
    user = await get_user_by_username(session, username)
    if user:
        if validate_password(password, user.password):
            return user
        else:
            raise WrongPasswordException
    else:
        raise UserNotFoundException


async def get_current_token_payload(
    token: str = Depends(oauth2_scheme),
) -> dict:
    try:
        payload = decode_jwt(
            token=token,
        )
    except InvalidTokenError:
        raise InvalidTokenException
    return payload


async def get_current_user(
    payload: dict = Depends(get_current_token_payload),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> User:
    username = payload.get("sub")
    user = await get_user_by_username(username=username, session=session)
    if user:
        return user
    else:
        raise InvalidTokenException


async def get_current_active_user(
    user: User = Depends(get_current_user),
):
    if user.active:
        return user
    raise UserInactiveException
