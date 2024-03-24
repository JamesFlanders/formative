from typing import Optional, TYPE_CHECKING

from sqlalchemy import UniqueConstraint
from sqlmodel import Field, Relationship

from domain.group import Group
from infrastructure.models.user_group_link import UserGroupLink

if TYPE_CHECKING:
    from infrastructure.models.user_model import UserModel


class GroupModel(Group, table=True):
    __tablename__ = "groups"
    __table_args__ = (UniqueConstraint('name'), {"schema": "public"})

    id: Optional[int] = Field(default=None, primary_key=True)

    users: list["UserModel"] = Relationship(back_populates="groups", link_model=UserGroupLink)
