from fastapi import APIRouter
from core.config import settings
from api.dependencies.authentication.fastapi_users import fastapi_users
from api.dependencies.authentication.backend import authentication_backends

router = APIRouter(
    prefix=settings.api.v1.auth,
    tags=["Auth"],
)
router.include_router(
    fastapi_users.get_auth_router(authentication_backends),
)
