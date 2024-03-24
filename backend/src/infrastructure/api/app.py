from litestar import Litestar, Router
from litestar.di import Provide

from infrastructure.api.controllers.authentication_controller import AuthenticationController
from infrastructure.api.controllers.group_controller import GroupController
from infrastructure.api.controllers.user_controller import UserController
from infrastructure.api.lifespan import provide_lifespan
from infrastructure.api.service import provide_formative_service
from infrastructure.api.transaction import provide_transaction

from infrastructure.models.user_model import UserModel  # noqa
from infrastructure.models.group_model import GroupModel  # noqa

authentication_router: Router = Router(
    path="/",
    tags=["authentication"],
    route_handlers=[AuthenticationController],
    dependencies={
        "service": Provide(provide_formative_service)
    }
)

admin_router: Router = Router(
    path="/admin",
    tags=["admin"],
    route_handlers=[UserController, GroupController],
    dependencies={
        "service": Provide(provide_formative_service)
    }
)

app = Litestar(
    route_handlers=[authentication_router, admin_router],
    dependencies={"transaction": provide_transaction},
    lifespan=[provide_lifespan],
    debug=True
)
