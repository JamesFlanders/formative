from litestar import Controller, post
from litestar.status_codes import HTTP_202_ACCEPTED, HTTP_204_NO_CONTENT

from infrastructure.api.schemas.login_schema import LoginSchema
from infrastructure.api.schemas.logout_schema import LogoutSchema
from service.formative_service import FormativeService


class AuthenticationController(Controller):
    @post(path="/login", status_code=HTTP_202_ACCEPTED)
    async def login(self, service: FormativeService, data: LoginSchema) -> None:
        raise NotImplementedError

    @post(path="/logout", status_code=HTTP_204_NO_CONTENT)
    async def logout(self, service: FormativeService, data: LogoutSchema) -> None:
        raise NotImplementedError
