from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text,
    text,
)
from sqlalchemy.dialects.postgresql import UUID

from core import database as db


class Category(db.Model):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    slug = Column(String(200), unique=True, nullable=False)
    is_active = Column(Boolean, default=False)
    parent_id = Column(Integer, ForeignKey("category.id"))


class Product(db.Model):
    __table_name__ = "product"

    id = Column(Integer, primary_key=True)
    pid = Column(
        UUID(as_uuid=True),
        unique=True,
        nullable=False,
        server_default=text("uuid_generate_v4()"),
    )
    name = Column(String(200), unique=True, nullable=False)
    slug = Column(String(255), unique=True, nullable=False)
    description = Column(Text)
    is_digital = Column(Boolean, default=False)
    created_at = Column(DateTime, server_default=db.text("CURRENT_TIMESTAMP"))
    update_at = Column(
        DateTime, server_default=db.text("CURRENT_TIMESTAMP"), onupdate=db.func.now()
    )
    is_active = Column(Boolean, default=False)
    stock_status = Column(String(100), default="OUT_OF_STOCK")
    category_id = Column(Integer, ForeignKey("category.id"))

    def __repr__(self) -> str:
        return f"<Name: {self.name}>"
