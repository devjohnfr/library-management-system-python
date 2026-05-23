from sqlalchemy.orm import Session

from app.repositories.book_repository import BookRepository
from app.schemas.book_schema import BookCreate

class BookService:

    @staticmethod
    def create_book(db: Session, book_data: BookCreate):
        return BookRepository.create(db, book_data)

    @staticmethod
    def list_books(db: Session):
        return BookRepository.get_all(db)