from dependency_injector import containers, providers

from app.application.services.books_service import BooksService
from app.infrastructure.repositories.book_repository import SQLAlchemyBookRepository

from sqlalchemy.orm import sessionmaker, scoped_session

from app.infrastructure.sqlalchemy_engine_factory import SQLAlchemyEngineFactory

SessionLocal = scoped_session(sessionmaker(
    autocommit=False, autoflush=False, bind=SQLAlchemyEngineFactory.create_engine()))


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
