from sqlalchemy import Engine, create_engine

import os
from dotenv import load_dotenv


class SQLAlchemyEngineFactory:
    @staticmethod
    def create_engine() -> Engine:
        load_dotenv()
        db_url = os.environ["DATABASE_URL"]
        if not db_url:
            raise ValueError("DATABASE_URL environment variable is not set")
        return create_engine(db_url)
