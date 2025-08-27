from typing import Optional
from app.domain.exceptions import ItemAlreadyExistsError, ItemNotFoundError
from app.domain.repositories.book_repository import BookRepository
from app.domain.models import Book
from app.infrastructure.models import BookORM
from sqlalchemy.exc import IntegrityError


class SQLAlchemyBookRepository(BookRepository):
    def __init__(self, session):
        self.session = session

    def get_book(self, book_id: int) -> Book:
        book_orm = self.session.query(BookORM).filter(
            BookORM.id == book_id).first()
        if book_orm:
            return Book.model_validate(book_orm)
        raise ItemNotFoundError(f"Book with id {book_id} not found")

    def get_books(self, title: Optional[str] = None, min_pages: Optional[int] = None) -> list[Book]:
        query = self.session.query(BookORM)
        if title:
            query = query.filter(BookORM.title.ilike(f"%{title}%"))
        if min_pages:
            query = query.filter(BookORM.pages >= min_pages)
        books_orm = query.all()
        return [Book.model_validate(b) for b in books_orm]

    def create_book(self, book: Book) -> Book:
        try:
            book_orm = BookORM(**book.model_dump())
            self.session.add(book_orm)
            self.session.commit()
            self.session.refresh(book_orm)
            return Book.model_validate(book_orm)
        except IntegrityError:
            self.session.rollback()
            raise ItemAlreadyExistsError(
                f"Book with title '{book.title}' and author '{book.author}' already exists.")

    def update_book(self, book_id: int, book_data: dict) -> Book:
        book_orm = self.session.query(BookORM).filter(
            BookORM.id == book_id).first()
        if not book_orm:
            raise ItemNotFoundError(f"Book with id {book_id} not found")
        for key, value in book_data.items():
            setattr(book_orm, key, value)
        self.session.commit()
        self.session.refresh(book_orm)
        return Book.model_validate(book_orm)

    def delete_book(self, book_id: int) -> bool:
        book_orm = self.session.query(BookORM).filter(
            BookORM.id == book_id).first()
        if not book_orm:
            raise ItemNotFoundError(f"Book with id {book_id} not found")
        self.session.delete(book_orm)
        self.session.commit()
        return True
