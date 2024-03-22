from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession


class DatabaseRepository:

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_model(self, model):
        self.session.add(model)

    async def get_all_models(self, model, offset: int = None, limit: int = None, **fields):
        query = select(model)
        query = self.__query_fields(query, model, **fields)
        query = self.__add_paging_to_query(query, offset, limit)
        result = await self.session.execute(query)
        return result.scalars()

    async def get_model(self, model, **fields):
        query = select(model)
        query = self.__query_fields(query, model, **fields)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()

    async def get_models(self, model, **fields):
        query = select(model)
        query = self.__query_fields(query, model, **fields)
        result = await self.session.execute(query)
        return result.scalars().all()

    async def update_model(self, model, model_attribute, model_value, **fields):
        model_field = getattr(model, model_attribute)
        query = select(model).where(model_field == model_value)
        result = await self.session.execute(query)
        model = result.scalar_one()
        for field, value in fields.items():
            setattr(model, field, value)
        self.session.add(model)
        return model

    async def delete_model(self, model, **fields):
        model = await self.get_model(model, **fields)
        await self.session.delete(model)

    @staticmethod
    def __add_paging_to_query(query, offset: int = None, limit: int = None):
        if offset and limit:
            query = query.limit(limit).offset((offset - 1) * limit)
        return query

    @staticmethod
    def __query_fields(query, model, **fields):
        for field_name, field_value in fields.items():
            model_field = getattr(model, field_name)
            query = query.where(model_field == field_value)
        return query
