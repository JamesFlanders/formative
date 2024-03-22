from litestar.datastructures import State
from litestar.exceptions import ClientException
from litestar.status_codes import HTTP_409_CONFLICT
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlmodel.ext.asyncio.session import AsyncSession

session_maker = async_sessionmaker(class_=AsyncSession, expire_on_commit=False)


async def provide_transaction(state: State):
    async with session_maker(bind=state.engine) as session:
        try:
            async with session.begin():
                yield session
        except IntegrityError as exc:
            __handle_integrity_error(exc)


def __handle_integrity_error(exc: IntegrityError):
    raise ClientException(
        status_code=HTTP_409_CONFLICT,
        detail=str(exc)
    ) from exc
