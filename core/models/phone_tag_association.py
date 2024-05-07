from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import mapped_column, Mapped

from core.models import Base


class PhoneTagAssociation(Base):
    __tablename__ = "phone_tag_association"
    __table_args__ = (UniqueConstraint(
        "phone_id", "tag_id", name="idx_unique_tag_phone"
    ),)

    id: Mapped[int] = mapped_column(primary_key=True)
    phone_id: Mapped[int] = mapped_column(ForeignKey("phones.id"))
    tag_id: Mapped[int] = mapped_column(ForeignKey("tags.id"))
