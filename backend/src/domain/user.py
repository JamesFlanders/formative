from sqlmodel import SQLModel


class User(SQLModel):
    username: str
    first_name: str
    last_name: str
    email: str
    password: str
