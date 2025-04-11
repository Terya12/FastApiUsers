from fastapi import Depends
from fastapi import APIRouter

from core.config import settings

router = APIRouter(
    prefix=settings.api.v1.messages,
    tags=["Messages"],
)


@router.get("/")
async def get_user_masseges():
    pass