from sqlalchemy.orm import mapped_column, Mapped, relationship
from typing import TYPE_CHECKING
from core.models import Base
if TYPE_CHECKING:
    from .phone import Product


class Tag(Base):
    __tablename__ = "tags"

    tag_name: Mapped[str] = mapped_column(unique=True)
    phones: Mapped[list["Product"]] = relationship(
        back_populates="tags", secondary="phone_tag_association"
    )
