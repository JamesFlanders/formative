from typing import Optional, TYPE_CHECKING

from sqlalchemy import UniqueConstraint
from sqlmodel import Field, Relationship

from domain.user import User
from infrastructure.models.user_group_link import UserGroupLink

if TYPE_CHECKING:
    from infrastructure.models.group_model import GroupModel


class UserModel(User, table=True):
    __tablename__ = "users"
    __table_args__ = (UniqueConstraint('username'), {"schema": "public"})

    id: Optional[int] = Field(default=None, primary_key=True)

    groups: list["GroupModel"] = Relationship(back_populates="users", link_model=UserGroupLink)
