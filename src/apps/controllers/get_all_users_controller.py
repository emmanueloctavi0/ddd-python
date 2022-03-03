from users.application.get_all_users import GetAllUsers
from users.infrastructure.postgresql import SqlAlchemyUserRepository
from users.infrastructure.postgresql import db


def get_all_users_controller():
    get_all_users = GetAllUsers(SqlAlchemyUserRepository(db.session))
    users = get_all_users.execute()
    return users
