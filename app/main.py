from fastapi import FastAPI
from app.database.connection import engine, Base
from app.models.book import Book

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Library Management System API"}