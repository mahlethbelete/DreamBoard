from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database import Base
from models.mixins import TimestampMixin


class User(Base, TimestampMixin):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(60), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(60), nullable=False)

    categories = relationship(
        "Category", back_populates="user", cascade="all, delete-orphan"
    )
    vision_items = relationship(
        "VisionItem", back_populates="user", cascade="all, delete-orphan"
    )
