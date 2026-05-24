from pydantic import BaseModel, Field


class BookBase(BaseModel):
    title: str = Field(..., min_length=2, max_length=100)
    author: str = Field(..., min_length=2, max_length=100)
    year: int = Field(..., ge=0, le=2100)
    available_copies: int = Field(..., ge=0)
    total_copies: int = Field(..., ge=1)

class BookCreate(BookBase):
    pass

class BookResponse(BookBase):
    id: int

    class Config:
        from_attributes = True