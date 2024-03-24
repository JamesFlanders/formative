from sqlmodel import SQLModel


class Group(SQLModel):
    name: str
