from sqlalchemy import (
    Column,
    Integer,
    String,
    TIMESTAMP,
    func,
    ForeignKey,
    Numeric
)
from sqlalchemy.orm import relationship

from src.database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, unique=True)
    description = Column(String)
    price = Column(Numeric(10, 2), nullable=False)
    quantity = Column(Integer, default=0)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())

    category_id = Column(Integer, ForeignKey("categories.id"), nullable=True)
    category = relationship("Category", back_populates="products")

    def __repr__(self):
        return f"Product: {self.name} ({self.price})"


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, unique=True)

    products = relationship("Product", back_populates="category")

    def __repr__(self):
        return f"Category name: {self.name}"
