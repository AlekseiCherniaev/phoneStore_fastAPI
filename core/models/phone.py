from typing import TYPE_CHECKING
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .category import Category
    from .tag import Tag


class Product(Base):
    __tablename__ = "phones"

    name: Mapped[str] = mapped_column(unique=True)
    price: Mapped[int]
    description: Mapped[str] = mapped_column(String(30), nullable=True)
    counts: Mapped[int] = mapped_column(default=0, server_default="0")
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))

    category: Mapped["Category"] = relationship(back_populates="phones")

    tags: Mapped[list["Tag"]] = relationship(
        back_populates="phones", secondary="phone_tag_association"
    )
