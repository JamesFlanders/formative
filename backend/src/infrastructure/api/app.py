from litestar import Litestar, Router
from litestar.di import Provide

from infrastructure.api.controllers.role_controller import RoleController
from infrastructure.api.controllers.user_controller import UserController
from infrastructure.api.lifespan import provide_lifespan
from infrastructure.api.service import provide_formative_service
from infrastructure.api.transaction import provide_transaction

from infrastructure.models.user_model import User  # noqa
from infrastructure.models.role_model import Role  # noqa

user_router: Router = Router(
    path="/user",
    tags=["user"],
    route_handlers=[UserController],
    dependencies={
        "service": Provide(provide_formative_service)
    }
)

role_router: Router = Router(
    path="/role",
    tags=["role"],
    route_handlers=[RoleController],
    dependencies={
        "service": Provide(provide_formative_service)
    }

)

app = Litestar(
    route_handlers=[user_router, role_router],
    dependencies={"transaction": provide_transaction},
    lifespan=[provide_lifespan]
)
