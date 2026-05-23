from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.book_schema import BookCreate, BookResponse
from app.services.book_service import BookService

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