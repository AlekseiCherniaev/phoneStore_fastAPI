from typing import Annotated
from annotated_types import MinLen, MaxLen
from pydantic import BaseModel, EmailStr, ConfigDict


class CreateUser(BaseModel):
    username: str
    password: str
    email: EmailStr | None = None


class UserSchema(BaseModel):
    model_config = ConfigDict(strict=True)
    username: str
    email: EmailStr | None = None
    active: bool | None = True


class UserInBD(UserSchema):
    hashed_password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None
