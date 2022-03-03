from users.domain.entities import User
from users.domain.user_repository import UserRepository


class CreateUser:

    def __init__(self, repository: UserRepository):
        self.repository = repository

    def execute(self, user_data: dict) -> User:
        user = User(**user_data)
        user = self.repository.save(user)
        self.repository.commit()
        return user
