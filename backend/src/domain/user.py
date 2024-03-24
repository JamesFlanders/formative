from typing import Optional

from sqlmodel import SQLModel, Field

from domain.role import Role


class User(SQLModel):
    username: str
    first_name: Optional[str] = Field(default=None)
    last_name: Optional[str] = Field(default=None)
    email: Optional[str] = Field(default=None)
    role: Role
    password: str
