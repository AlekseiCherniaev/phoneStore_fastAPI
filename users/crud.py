from fastapi import Depends
from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import AsyncSession
from auth import utils
from core.models import User, db_helper
from users.schemas import CreateUser


async def create_user(user_in: CreateUser, session: AsyncSession) -> User:
    user_data = user_in.model_dump()
    user_data["password"] = utils.hash_password(user_data["password"])
    user = User(**user_data)
    session.add(user)
    await session.commit()
    return user


async def get_user(session: AsyncSession, username: str) -> User | None:
    statement = select(User).where(User.username == username)
    result: Result = await session.execute(statement)
    user = result.scalar_one_or_none()
    print(user)
    return user
