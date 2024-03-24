from sqlmodel import SQLModel

from domain.role import Role


class User(SQLModel):
    username: str
    first_name: str
    last_name: str
    email: str
    role: Role
    password: str
