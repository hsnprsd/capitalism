from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from db.db import Base


class Category(Base):
    __tablename__ = 'categories'

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )
    name = Column(
        String,
        nullable=False,
    )


class Asset(Base):
    __tablename__ = 'assets'

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )
    category_id = Column(
        Integer,
        ForeignKey('categories.id'),
        nullable=False,
    )
    category = relationship('Category')
    amount = Column(
        Float,
        nullable=False,
        default=0,
    )
