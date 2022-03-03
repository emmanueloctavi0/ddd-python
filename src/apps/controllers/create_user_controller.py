from users.application.create_user import CreateUser
from users.infrastructure.postgresql import SqlAlchemyUserRepository
from users.infrastructure.postgresql import db


def create_user_controller(data):
    create_user = CreateUser(SqlAlchemyUserRepository(db.session))
    return create_user.execute(data)
