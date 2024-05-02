from sqlalchemy import String, CheckConstraint, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Product(Base):
    __tablename__ = "phones"

    name: Mapped[str] = mapped_column(unique=True)
    price: Mapped[int]
    description: Mapped[str] = mapped_column(String(30), nullable=True)
    counts: Mapped[int] = mapped_column(default=0, server_default="0")
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))
