from fastapi import APIRouter
from core.config import settings
from api.dependencies.authentication.fastapi_users import fastapi_users
from api.dependencies.authentication.backend import authentication_backends
from core.schemas.user import (
    UserRead,
    UserCreate,
)


router = APIRouter(
    prefix=settings.api.v1.auth,
    tags=["Auth"],
)

# /login
# /logout

router.include_router(
    fastapi_users.get_auth_router(
        authentication_backends,
    ),
)

# /register
router.include_router(
    fastapi_users.get_register_router(
        UserRead,
        UserCreate,
    ),
)
