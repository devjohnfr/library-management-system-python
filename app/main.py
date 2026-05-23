from fastapi import FastAPI

from app.database.connection import engine, Base
from app.models.book import Book
from app.routes.book_routes import router as book_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Library Management System",
    version="1.0.0"
)

app.include_router(book_router)

@app.get("/")
def home():
    return {"message": "Library Management System API"}