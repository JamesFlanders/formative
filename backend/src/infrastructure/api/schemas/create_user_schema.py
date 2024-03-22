from litestar.exceptions import ClientException
from pydantic import model_validator

from domain.user import User


class CreateUserSchema(User):
    password_confirmation: str

    @model_validator(mode='after')
    def check_passwords_match(self) -> 'CreateUserSchema':
        if not self.password or not self.password_confirmation:
            raise ValueError("Both password fields are required!")
        if self.password != self.password_confirmation:
            raise ClientException('Passwords do not match')
        return self
