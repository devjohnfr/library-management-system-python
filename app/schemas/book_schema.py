from pydantic import BaseModel


class BookBase(BaseModel):
    title: str
    author: str
    year: int
    available_copies: int
    total_copies: int


class BookCreate(BookBase):
    pass


class BookResponse(BookBase):
    id: int

    class Config:
        from_attributes = True