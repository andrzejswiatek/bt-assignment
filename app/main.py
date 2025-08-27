from contextlib import asynccontextmanager
from fastapi import FastAPI
from sqlalchemy import create_engine
from app.api.routes.books import books_router
from app.container import CoreContainer
from app.infrastructure.models import Base


def create_app() -> FastAPI:
    # TODO: move to the configuration
    DATABASE_URL = "postgresql://assesment:secretforassesment@localhost:5432/assesment"
    # TODO: consider encapsulation
    engine = create_engine(DATABASE_URL)

    @asynccontextmanager
    async def lifespan(app: FastAPI):
        Base.metadata.create_all(bind=engine)
        yield

    app = FastAPI(lifespan=lifespan)
    app.include_router(books_router)
    container = CoreContainer()

    container.wire(modules=[__name__, "app.api.routes.books"])

    return app


app = create_app()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app,
        host="127.0.0.1",
        port=8080,
        log_config=None,
    )
