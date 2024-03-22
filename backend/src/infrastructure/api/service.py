from sqlalchemy.ext.asyncio import AsyncSession

from infrastructure.repositories.role_database_repository import RoleDatabaseRepository
from infrastructure.repositories.user_database_repository import UserDatabaseRepository
from service.formative_service import FormativeService


async def provide_formative_service(transaction: AsyncSession) -> FormativeService:
    return FormativeService(
        user_repository=UserDatabaseRepository(transaction),
        role_repository=RoleDatabaseRepository(transaction),
    )
