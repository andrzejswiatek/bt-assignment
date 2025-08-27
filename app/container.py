from dependency_injector import containers, providers

from app.application.services.books_service import BooksService
from app.infrastructure.repositories.book_repository import SQLAlchemyBookRepository

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

DATABASE_URL = "postgresql://assesment:secretforassesment@localhost:5432/assesment"
engine = create_engine(DATABASE_URL)
SessionLocal = scoped_session(sessionmaker(
    autocommit=False, autoflush=False, bind=engine))


class CoreContainer(containers.DeclarativeContainer):
    db_session = providers.Singleton(SessionLocal)
    books_repository = providers.Factory(
        SQLAlchemyBookRepository,
        session=db_session
    )
    books_service = providers.Factory(
        BooksService,
        books_repository=books_repository
    )
