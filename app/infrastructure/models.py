from sqlalchemy import Float, Integer, String, UniqueConstraint
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BookORM(Base):
    __tablename__ = "books"
    __table_args__ = (
        UniqueConstraint("title", "author", name="uq_books_title_author"),
    )
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=False)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    author: Mapped[str] = mapped_column(String(100), nullable=False)
    pages: Mapped[int] = mapped_column(Integer, nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=False)
