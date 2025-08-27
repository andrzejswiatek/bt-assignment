from typing import Annotated, Optional
from fastapi import APIRouter, HTTPException, Depends
from app.api.models import BookInput, BookOutput, BookUpdateModel
from app.domain.exceptions import ItemAlreadyExistsError, ItemNotFoundError
from app.container import CoreContainer
from app.domain.models import Book
from app.domain.services.books_service_interface import BooksServiceProtocol


from dependency_injector.wiring import inject, Provide

books_router = APIRouter()


@books_router.get("/health")
def health_check():
    return {"status": "ok"}


@books_router.get("/books/{book_id}")
@inject
def get_book(book_id: int, book_service: Annotated[BooksServiceProtocol, Depends(Provide["books_service"])]):
    try:
        book = book_service.get_book(book_id)
        return book
    except ItemNotFoundError:
        raise HTTPException(status_code=404, detail="Book not found")


@books_router.get("/books")
@inject
def get_books(book_service: Annotated[BooksServiceProtocol, Depends(Provide[CoreContainer.books_service])], title: Optional[str] = None, min_pages: Optional[int] = None):
    books = book_service.get_books(title=title, min_pages=min_pages)
    return books


@books_router.post("/books", status_code=201)
@inject
def create_book(
    book: BookInput,
    book_service: Annotated[BooksServiceProtocol,
                            Depends(Provide[CoreContainer.books_service])]
) -> BookOutput:
    new_book: Book = Book(**book.model_dump())
    try:
        result = book_service.create_book(new_book)
        return BookOutput.model_validate(result.model_dump())
    except ItemAlreadyExistsError:
        raise HTTPException(status_code=409, detail="Book already exists")


@books_router.put("/books/{book_id}")
@inject
def update_book(book_id: int, book_update: BookUpdateModel, book_service: Annotated[BooksServiceProtocol, Depends(Provide[CoreContainer.books_service])]) -> BookOutput:
    try:
        book_service.get_book(book_id)
        book_data = book_update.dict(exclude_unset=True)
        if not book_data:
            raise HTTPException(
                status_code=400, detail="No property for update provided")

        result = book_service.update_book(book_id, book_data)
        return BookOutput.model_validate(result.model_dump())
    except ItemNotFoundError:
        raise HTTPException(status_code=404, detail="Book not found")


@books_router.delete("/books/{book_id}", status_code=204)
@inject
def delete_book(book_id: int, book_service: Annotated[BooksServiceProtocol, Depends(Provide[CoreContainer.books_service])]):
    try:
        book_service.delete_book(book_id)
        return {"detail": "Book deleted successfully"}
    except ItemNotFoundError:
        raise HTTPException(status_code=404, detail="Book not found")
