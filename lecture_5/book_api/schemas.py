from pydantic import BaseModel
from typing import Optional


class BookBase(BaseModel):
    """
    Base schema for a Book
    """

    title: str  # Title of the Book
    author: str  # Author of the Book
    year: Optional[int] = None  # Publication year of the Book (optional)


class BookCreate(BookBase):
    """
    Schema for creating/updating a Book
    """

    pass


class BookResponse(BookBase):
    """
    Schema for responding with Book data
    """

    id: int  # ID field for the Book

    class Config:
        """
        Configuration for Pydantic model to work with ORM objects
        """

        from_attributes = True
