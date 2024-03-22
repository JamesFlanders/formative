from typing import Optional, TYPE_CHECKING

from sqlalchemy import UniqueConstraint
from sqlmodel import Field, Relationship

from domain.user import User
from infrastructure.models.user_role_link import UserRoleLink

if TYPE_CHECKING:
    from infrastructure.models.role_model import RoleModel


class UserModel(User, table=True):
    __tablename__ = "users"
    __table_args__ = (UniqueConstraint('username'), {"schema": "public"})

    id: Optional[int] = Field(default=None, primary_key=True)

    roles: list["RoleModel"] = Relationship(back_populates="users", link_model=UserRoleLink)
