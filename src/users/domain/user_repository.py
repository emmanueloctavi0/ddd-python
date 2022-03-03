from abc import ABC, abstractmethod
from typing import List
from users.domain.entities import User


class UserRepository(ABC):

    @abstractmethod
    def save(self, user: User) -> User:
        raise NotImplementedError

    @abstractmethod
    def all(self) -> List[User]:
        raise NotImplementedError

    @abstractmethod
    def commit(self) -> None:
        raise NotImplementedError
