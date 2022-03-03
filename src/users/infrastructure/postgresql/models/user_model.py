import uuid
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.dialects.postgresql import UUID

from users.infrastructure.postgresql.db import Base


class UserModel(Base):
    __tablename__ = "users"

    id = Column(String(36), primary_key=True, default=uuid.uuid4)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
