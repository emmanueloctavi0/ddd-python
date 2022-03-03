from flask import Blueprint
from flask import request
from flask import jsonify

from apps.controllers import get_all_users_controller
from apps.controllers import create_user_controller


bp = Blueprint('users', __name__, url_prefix='/users')


@bp.route('/', methods=['GET'])
def get_users():
    users = get_all_users_controller()
    users = [user.to_dict() for user in users]
    return jsonify(users)


@bp.route('/', methods=['POST'])
def create_user():
    body = request.get_json()
    user = create_user_controller(body)
    return user.to_dict()
