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

    @staticmethod
    def update(db: Session, book_id: int, book_data):
        book = db.query(Book).filter(Book.id == book_id).first()

        if not book:
            return None

        for key, value in book_data.model_dump().items():
            setattr(book, key, value)

        db.commit()
        db.refresh(book)

        return book

    @staticmethod
    def delete(db: Session, book_id: int):
        book = db.query(Book).filter(Book.id == book_id).first()

        if not book:
            return None

        db.delete(book)
        db.commit()

        return book