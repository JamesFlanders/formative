import pytest
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlmodel import SQLModel
from testcontainers.postgres import PostgresContainer

from domain.role import Role
from domain.user import User
from infrastructure.models.role_model import RoleModel
from infrastructure.models.user_model import UserModel


async def __create_database(engine):
    async with engine.begin() as connection:
        await connection.run_sync(SQLModel.metadata.create_all)


async def __drop_database(engine):
    async with engine.begin() as connection:
        await connection.run_sync(SQLModel.metadata.drop_all)


async def __populate_database_with_test_data(session):
    users: list[User] = [
        User(username="michaels", email="michael.scott@dundermifflin.com", first_name="Michael", last_name="Scott",
             password="littlekidlover!"),
        User(username="jimh", email="jim.halpert@dundermifflin.com", first_name="Jim", last_name="Halpert",
             password="il0v3p4m!"),
    ]
    user_models: list[UserModel] = [UserModel.model_validate(user) for user in users]
    roles: list[Role] = [Role(name="admin"), Role(name="user"), Role(name="guest")]
    role_models: list[RoleModel] = [RoleModel.model_validate(role) for role in roles]
    session.add_all(user_models)
    session.add_all(role_models)
    await session.commit()


@pytest.fixture
def database_container():
    with PostgresContainer("postgres:16.2-alpine3.19") as container:
        yield container


@pytest.fixture
async def engine(database_container):
    url = database_container.get_connection_url(driver="asyncpg")
    engine = create_async_engine(url)
    await __create_database(engine)
    yield engine
    await __drop_database(engine)
    await engine.dispose()


@pytest.fixture
async def session(engine):
    session_maker = async_sessionmaker(autoflush=True, autocommit=False, bind=engine)
    async with session_maker() as session:
        try:
            await __populate_database_with_test_data(session)
            yield session
        except IntegrityError:
            await session.rollback()
        finally:
            await session.close()
