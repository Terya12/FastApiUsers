from typing import TYPE_CHECKING, Annotated
from fastapi import Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase, SQLAlchemyAccesTokenDatabase
from core.models.db_helper import db_helper
from core.models.user import User
if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession
from core.models.access_token import AccessToken

async def get_access_tokens_db(
    session: Annotated[
    AsyncSession,
    Depends(db_helper.session_getter)
    ]
):
    yield AccessToken.get_db(session=session)