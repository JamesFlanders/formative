from litestar.exceptions import ClientException
from pydantic import model_validator, BaseModel


class UpdateUserPasswordSchema(BaseModel):
    old_password: str
    new_password: str
    new_password_confirmation: str

    @model_validator(mode='after')
    def check_passwords_match(self) -> 'UpdateUserPasswordSchema':
        if not self.old_password:
            raise ClientException("Old password is required!")
        if not self.new_password or not self.new_password_confirmation:
            raise ClientException("Both new passwords fields are required!")
        if self.new_password != self.new_password_confirmation:
            raise ClientException('New passwords do not match')
        return self
