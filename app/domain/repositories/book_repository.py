from typing import Optional, Protocol

from app.domain.models import Book

class BookRepositoryProtocol(Protocol):
    def get_book(self, book_id: int) -> Book:
        ...

    def get_books(self, title: Optional[str] = None, min_pages: Optional[int] = None) -> list[Book]:
        ...

    def create_book(self, book: Book) -> Book:
        ...

    def update_book(self, book_id: int, book_data: dict) -> Book:
        ...

    def delete_book(self, book_id: int) -> bool:
        ...