from sqlalchemy import Column, ForeignKey, Integer, String

from .database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, index=True)
    selling_price = Column(Integer, nullable=False)
    purchase_price = Column(Integer, nullable=False)
    stock = Column(Integer, nullable=False)