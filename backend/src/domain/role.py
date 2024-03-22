from sqlmodel import SQLModel


class Role(SQLModel):
    name: str
