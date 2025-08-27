from app.infrastructure.models import BookORM, Base
from app.infrastructure.sqlalchemy_engine_factory import SQLAlchemyEngineFactory
from sqlalchemy.orm import sessionmaker

BOOKS = [
    BookORM(id=1, title="To Kill a Mockingbird", author="Harper Lee", pages=324, rating=4.8, price=14.99),
    BookORM(id=2, title="1984", author="George Orwell", pages=328, rating=4.7, price=12.95),
    BookORM(id=3, title="Animal Farm", author="George Orwell", pages=112, rating=4.6, price=8.99),
    BookORM(id=4, title="Pride and Prejudice", author="Jane Austen", pages=279, rating=4.6, price=9.99),
    BookORM(id=5, title="The Great Gatsby", author="F. Scott Fitzgerald", pages=180, rating=4.4, price=10.99),
]

def seed_books():
    engine = SQLAlchemyEngineFactory.create_engine()
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for book in BOOKS:
        exists = session.query(BookORM).filter_by(id=book.id).first()
        if not exists:
            session.add(book)
    session.commit()
    session.close()
    print("Books seeded successfully.")

if __name__ == "__main__":
    seed_books()
