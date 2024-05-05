from pydantic import EmailStr
from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped

from core.models import Base


class User(Base):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column(nullable=True)
    password: Mapped[bytes]
    active: Mapped[bool] = mapped_column(default=True)

