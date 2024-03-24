from pydantic import BaseModel


class LogoutSchema(BaseModel):
    username: str
