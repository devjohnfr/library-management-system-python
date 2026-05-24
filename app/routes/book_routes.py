from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.schemas.book_schema import BookCreate, BookResponse
from app.services.book_service import BookService
from fastapi import APIRouter, Depends

router = APIRouter(
    prefix="/books",
    tags=["Books"]
)

@router.post("/", response_model=BookResponse)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    return BookService.create_book(db, book)

@router.get("/", response_model=list[BookResponse])
def list_books(db: Session = Depends(get_db)):
    return BookService.list_books(db)

@router.put("/{book_id}", response_model=BookResponse)
def update_book(book_id: int, book: BookCreate, db: Session = Depends(get_db)):
    return BookService.update_book(db, book_id, book)


@router.delete("/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    return BookService.delete_book(db, book_id)