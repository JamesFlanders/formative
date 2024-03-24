from typing import Optional

from sqlmodel import SQLModel, Field


class UserGroupLink(SQLModel, table=True):
    __tablename__ = "user_group_links"

    user_id: Optional[int] = Field(default=None, foreign_key="public.users.id", primary_key=True)
    group_id: Optional[int] = Field(default=None, foreign_key="public.groups.id", primary_key=True)
