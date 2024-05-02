from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import User, db_helper
from users.schemas import CreateUser


async def create_user(user_in: CreateUser, session: AsyncSession) -> User:
    user = User(**user_in.model_dump())
    session.add(user)
    await session.commit()
    return user
