from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from typing import Generator

# Define the database model
Base = declarative_base()


# Define the Book model
class Book(Base):
    __tablename__ = "books"  # name of the table in the database

    # id: integer, primary key
    id = Column(Integer, primary_key=True, index=True)

    # title: string (required)
    title = Column(String, nullable=False)

    # author: string (required)
    author = Column(String, nullable=False)

    # year: integer (optional)
    year = Column(Integer, nullable=True)

    # representation method for debugging
    def __repr__(self):
        return f"<Book(id={self.id}, title='{self.title}', author='{self.author}', year={self.year})>"


# Create the SQLite database
engine = create_engine('sqlite:///library.db', echo=True)

# Create local session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator[Session, None, None]:
    """
    Dependency that provides a database session
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
