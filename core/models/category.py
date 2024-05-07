from typing import TYPE_CHECKING
from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped, relationship

from core.models import Base

if TYPE_CHECKING:
    from .phone import Product


class Category(Base):
    __tablename__ = "categories"

    name: Mapped[str] = mapped_column(String(32), unique=True)
    description: Mapped[str] = mapped_column(String(128), default="", server_default="")

    phones: Mapped[list["Product"]] = relationship(back_populates="category")
