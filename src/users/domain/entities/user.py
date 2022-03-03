from dataclasses import dataclass
from dataclasses import field

from uuid import uuid4
from uuid import UUID


@dataclass
class User:
    name: str
    email: str
    id: UUID = field(default_factory=uuid4)

    def __repr__(self) -> str:
        return f"<User(name={self.name}; email={self.email})>"

    def __dict__(self) -> dict:
        return {
            "id": str(self.id),
            "name": self.name,
            "email": self.email,
        }

    def to_dict(self) -> dict:
        return self.__dict__()
