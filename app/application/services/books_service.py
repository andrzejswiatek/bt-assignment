from typing import Optional
from app.domain.models import Book
from app.domain.repositories.book_repository import BookRepositoryProtocol


class BooksService():
    def __init__(self, books_repository: BookRepositoryProtocol):
        self.books_repository = books_repository

    def get_book(self, book_id: int) -> Book:
        return self.books_repository.get_book(book_id)

    def get_books(self, title: Optional[str] = None, min_pages: Optional[int] = None) -> list[Book]:
        return self.books_repository.get_books(title, min_pages)

    def create_book(self, book: Book) -> Book:
        return self.books_repository.create_book(book)

    def update_book(self, book_id: int, book_data: dict) -> Book:
        return self.books_repository.update_book(book_id, book_data)

    def delete_book(self, book_id: int) -> bool:
        return self.books_repository.delete_book(book_id)
