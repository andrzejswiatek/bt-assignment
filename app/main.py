from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.api.routes.books import books_router
from app.container import CoreContainer
from app.infrastructure.models import Base
from app.infrastructure.sqlalchemy_engine_factory import SQLAlchemyEngineFactory
from app.middleware import setup_middlewares


def create_app() -> FastAPI:

    @asynccontextmanager
    async def lifespan(app: FastAPI):
        Base.metadata.create_all(bind=SQLAlchemyEngineFactory.create_engine())
        yield

    app = FastAPI(lifespan=lifespan)
    app.include_router(books_router)
    container = CoreContainer()

    container.wire(modules=[__name__, "app.api.routes.books"])

    return app


app = create_app()

setup_middlewares(app)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app,
        host="127.0.0.1",
        port=8080,
        log_config=None,
    )
