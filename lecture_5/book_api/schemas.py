from pydantic import BaseModel
from typing import Optional


class BookBase(BaseModel):
    """
    Base schema for a Book
    """

    title: str
    author: str
    year: Optional[int] = None


class BookCreate(BookBase):
    """
    Schema for creating/updating a Book
    """

    pass


class BookResponse(BookBase):
    """
    Schema for responding with Book data
    """

    id: int

    class Config:
        """
        Configuration for Pydantic model to work with ORM objects
        """

        from_attributes = True
