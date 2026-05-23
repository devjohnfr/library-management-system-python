from sqlalchemy.orm import Session

from app.models.book import Book
from app.schemas.book_schema import BookCreate

class BookRepository:

    @staticmethod
    def create(db, book_data):

        print(book_data)

        print(book_data.model_dump())

        new_book = Book(**book_data.model_dump())

        db.add(new_book)

        db.commit()

        db.refresh(new_book)

        return new_book

    @staticmethod
    def get_all(db: Session):
        return db.query(Book).all()

