
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from core.models.base import Base
from core.models.mixins.id_int_pk import IdIntPkMixin


class User(Base,IdIntPkMixin, SQLAlchemyBaseUserTable[int]):
    pass
