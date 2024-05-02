from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped

from core.models import Base


class User(Base):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(String(32), unique=True)
