from typing import List
from users.domain.entities import User
from users.domain.user_repository import UserRepository


class GetAllUsers:

    def __init__(self, repository: UserRepository):
        self.repository = repository

    def execute(self) -> List[User]:
        return self.repository.all()
