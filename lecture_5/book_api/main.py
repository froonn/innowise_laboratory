from http.client import HTTPException

from database import *
from schemas import *

from fastapi import FastAPI, Depends, Query, HTTPException

# Create the FastAPI app
app = FastAPI()

# Create the database tables
Base.metadata.create_all(bind=engine)


def get_book_or_404(book_id: int, db: Session) -> Book:
    """
    Retrieve a book by ID or raise a 404 error if not found.
    """

    # Query the book by ID
    db_book = db.query(Book).filter(Book.id == book_id).first()

    # If not found, raise 404 error
    if db_book is None:
        raise HTTPException(status_code=404, detail=f"Book with ID {book_id} not found")

    # Return the found book
    return db_book


@app.get("/")
def root():
    """
    Root endpoint providing a welcome message.
    """

    return {"message": "Welcome to the Book API! Use the /books endpoint to manage your book collection. Or use /docs for the API documentation."}

@app.post("/books", response_model=BookResponse)
def add_a_new_book(book: BookCreate, db: Session = Depends(get_db)):
    """
    Add a new book to the database.
    """

    # Create a new Book instance
    db_book = Book(title=book.title, author=book.author, year=book.year)
    db.add(db_book)

    # Save changes
    db.commit()
    db.refresh(db_book)

    # Return the newly created book
    return db_book


@app.get("/books", response_model=list[BookResponse])
def get_all_books(db: Session = Depends(get_db)):
    """
    Retrieve all books from the database.
    """

    # Query all books
    return db.query(Book).all()


@app.delete("/books/{book_id}")
def delete_a_book_by_id(book_id: int, db: Session = Depends(get_db)):
    """
    Delete a book by its ID.
    """

    # Retrieve the book or raise 404
    db_book = get_book_or_404(book_id, db)

    # Delete the book
    db.delete(db_book)
    db.commit()

    # Return a success message
    return {"message": f"Book with ID {book_id} deleted successfully"}


@app.put("/books/{book_id}", response_model=BookResponse)
def update_book_details(book_id: int, book_update: BookCreate, db: Session = Depends(get_db)):
    """
    Update the details of an existing book.
    """
    # Retrieve the book or raise 404
    db_book = get_book_or_404(book_id, db)

    # Update book details
    db_book.title = book_update.title
    db_book.author = book_update.author
    db_book.year = book_update.year

    # Save changes
    db.commit()
    db.refresh(db_book)

    # Return the updated book
    return db_book


@app.get("/books/search", response_model=list[BookResponse])
def search_books_by_title_or_author_or_year(
        title: Optional[str] = Query(None, description="Search by title"),
        author: Optional[str] = Query(None, description="Search by author"),
        year: Optional[int] = Query(None, description="Search by year"),
        db: Session = Depends(get_db)
):
    """
    Search books by title, author, or year.
    """
    query = db.query(Book)

    # Apply filters
    if title:
        query = query.filter(Book.title.contains(title))
    if author:
        query = query.filter(Book.author.contains(author))
    if year:
        query = query.filter(Book.year == year)

    # Return the filtered results
    return query.all()
