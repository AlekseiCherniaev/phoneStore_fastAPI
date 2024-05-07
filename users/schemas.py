from pydantic import BaseModel, EmailStr, ConfigDict


class CreateUser(BaseModel):
    username: str
    password: str
    email: EmailStr | None = None


class User(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    username: str
    password: str
    email: EmailStr | None = None
    active: bool | None = True


class Token(BaseModel):
    access_token: str
    token_type: str
