from fastapi import Depends, HTTPException, Form
from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import AsyncSession
from auth import utils
from auth.utils import validate_password
from core.models import User, db_helper
from users.schemas import SCreateUser, SUserLogin


async def create_user(user_in: SCreateUser, session: AsyncSession) -> User:
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
    return user


async def validate_user(username: str = Form(),
                        password: str = Form(),
                        session: AsyncSession = Depends(db_helper.scoped_session_dependency)) -> User:
    user_db = await get_user(session, username)
    if user_db:
        if validate_password(password, user_db.password):
            print('SUCCESS')
            return user_db
        else:
            raise HTTPException(status_code=404, detail="Wrong password")
    else:
        raise HTTPException(status_code=404, detail="User not found")
