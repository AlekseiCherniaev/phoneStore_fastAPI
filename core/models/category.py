from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped

from core.models import Base


class Category(Base):
    __tablename__ = "categories"

    name: Mapped[str] = mapped_column(String(32), unique=True)
    description: Mapped[str] = mapped_column(String(128), default="", server_default="")
