from sqlalchemy.orm import mapped_column, Mapped

from core.models import Base


class Tag(Base):
    __tablename__ = "tags"

    tag_name: Mapped[str] = mapped_column(unique=True)
