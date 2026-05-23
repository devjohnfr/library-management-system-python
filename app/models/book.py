from sqlalchemy import Column, Integer, String
from app.database.connection import Base

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(150), nullable=False)
    author = Column(String(100), nullable=False)
    year = Column(Integer, nullable=False)
    available_copies = Column(Integer, nullable=False)
    total_copies = Column(Integer, nullable=False)