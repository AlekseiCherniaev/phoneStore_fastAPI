from typing import Annotated
from annotated_types import MinLen, MaxLen
from pydantic import BaseModel, EmailStr, ConfigDict


class SCreateUser(BaseModel):
    username: str
    password: str
    email: EmailStr | None = None


class User(BaseModel):
    model_config = ConfigDict(strict=True)
    username: str
    email: EmailStr | None = None
    active: bool | None = True


class SUserInBD(User):
    password: str


class SUserLogin(BaseModel):
    username: str
    password: str


class SToken(BaseModel):
    access_token: str
    token_type: str


class STokenData(BaseModel):
    username: str | None = None
