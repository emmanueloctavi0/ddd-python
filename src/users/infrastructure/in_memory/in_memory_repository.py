from typing import List
from users.domain.user_repository import UserRepository
from users.domain.entities import User


class InMemoryUserRepository(UserRepository):
    users = []

    def save(self, user: User) -> User:
        self.users.append(user)
        return user

    def all(self) -> List[User]:
        return self.users

    def commit(self) -> None:
        pass
