import os
from contextlib import asynccontextmanager

from litestar import Litestar
from sqlalchemy import URL
from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel import SQLModel

PSQL_ASYNC_DRIVER = "postgresql+asyncpg"


@asynccontextmanager
async def provide_lifespan(app: Litestar):
    if engine := getattr(app.state, "engine", None) is None:
        url = __get_engine_url()
        engine = create_async_engine(url)
        app.state.engine = engine

    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

    try:
        yield
    finally:
        await engine.dispose()


def __get_engine_url():
    return URL.create(
        drivername=PSQL_ASYNC_DRIVER,
        username=os.environ["DATABASE_USER"],
        password=os.environ["DATABASE_PASSWORD"],
        database=os.environ["DATABASE_NAME"],
        host=os.environ["DATABASE_HOST"],
        port=int(os.environ["DATABASE_PORT"]),
    )