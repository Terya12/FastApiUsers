from fastapi import APIRouter
from core.config import settings
from api.dependencies.authentication.fastapi_users import fastapi_users

router = APIRouter(
    prefix=settings.api.v1.auth,
    tags=["Auth"],
)
