from litestar import Litestar

from infrastructure.api.controllers.role_controller import RoleController
from infrastructure.api.controllers.user_controller import UserController
from infrastructure.api.lifespan import provide_lifespan
from infrastructure.api.transaction import provide_transaction

from infrastructure.models.user_model import User  # noqa
from infrastructure.models.role_model import Role  # noqa

app = Litestar(
    route_handlers=[UserController, RoleController],
    dependencies={"transaction": provide_transaction},
    lifespan=[provide_lifespan]
)
