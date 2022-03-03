from typing import List
from users.domain.user_repository import UserRepository
from users.domain.entities import User
from users.infrastructure.postgresql.models import UserModel


class SqlAlchemyUserRepository(UserRepository):
    def __init__(self, db_session):
        self.db_session = db_session

    def save(self, user: User) -> User:
        user_model = UserModel(**user.to_dict())
        self.db_session.add(user_model)
        return user

    def all(self) -> List[User]:
        users_model = self.db_session.query(UserModel).all()
        users = []
        for user_model in users_model:
            user = User(
                id=user_model.id,
                name=user_model.name,
                email=user_model.email,
            )

            users.append(user)
        return users

    def commit(self):
        try:
            self.db_session.commit()
        except Exception as e:
            self.db_session.rollback()
            raise e
