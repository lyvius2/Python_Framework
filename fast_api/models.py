from sqlalchemy import Column, Integer, String, Float, Boolean
import database


class Product(database.Base):
    __tablename__ = 'product'
    product_no = Column(String, primary_key=True, index=True)
    product_name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    stock = Column(Integer, nullable=False)
