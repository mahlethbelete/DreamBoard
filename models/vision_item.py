import enum
from datetime import datetime

from sqlalchemy import Enum as SQLEnum
from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base
from models.mixins import TimestampMixin


class VisionStatus(str, enum.Enum):
    not_started = "not_started"
    in_progress = "in_progress"
    achieved = "achieved"


class VisionItem(Base, TimestampMixin):
    __tablename__ = "vision_items"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)

    category_id: Mapped[int] = mapped_column(
        ForeignKey("categories.id"), nullable=False
    )

    title: Mapped[str] = mapped_column(String, nullable=False)

    description: Mapped[str | None] = mapped_column(String, nullable=True)

    image_url: Mapped[str | None] = mapped_column(String, nullable=True)

    target_date: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True), nullable=True
    )

    status: Mapped[VisionStatus] = mapped_column(
        SQLEnum(VisionStatus, name="vision_status"),
        nullable=False,
        default=VisionStatus.not_started,
    )

    user = relationship("User", back_populates="vision_items")
    category = relationship("Category", back_populates="vision_items")
