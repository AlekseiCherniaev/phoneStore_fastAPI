from sqlalchemy import Table, Column, Integer, ForeignKey, UniqueConstraint

from core.models import Base

Phone_tag_association = Table(
    "phone_tag_association",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("phone_id", ForeignKey("phones.id")),
    Column("tag_id", ForeignKey("tags.id")),
    UniqueConstraint("phone_id", "tag_id"),
)
