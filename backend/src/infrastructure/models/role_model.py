from typing import Optional, TYPE_CHECKING

from sqlalchemy import UniqueConstraint
from sqlmodel import Field, Relationship

from domain.role import Role
from infrastructure.models.user_role_link import UserRoleLink

if TYPE_CHECKING:
    from infrastructure.models.user_model import UserModel


class RoleModel(Role, table=True):
    __tablename__ = "roles"
    __table_args__ = (UniqueConstraint('name'), {"schema": "public"})

    id: Optional[int] = Field(default=None, primary_key=True)

    users: list["UserModel"] = Relationship(back_populates="roles", link_model=UserRoleLink)
