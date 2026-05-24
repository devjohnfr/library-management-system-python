from sqlalchemy.orm import Session
from app.repositories.book_repository import BookRepository
from app.schemas.book_schema import BookCreate
from fastapi import HTTPException

class BookService:

    @staticmethod
    def create_book(db: Session, book_data: BookCreate):
        return BookRepository.create(db, book_data)

    @staticmethod
    def list_books(db: Session):
        return BookRepository.get_all(db)

    @staticmethod
    def update_book(db, book_id, book_data):
        updated_book = BookRepository.update(db, book_id, book_data)

        if not updated_book:
            raise HTTPException(status_code=404, detail="Book not found")

        return updated_book

    @staticmethod
    def delete_book(db, book_id):
        deleted_book = BookRepository.delete(db, book_id)

        if not deleted_book:
            raise HTTPException(status_code=404, detail="Book not found")

        return {"message": "Book deleted successfully"}