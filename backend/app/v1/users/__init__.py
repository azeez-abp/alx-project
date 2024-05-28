""" Blueprint for API """
from flask import Blueprint  # type: ignore
from flask_restful import Api  # type: ignore
from app.v1.users.login import UserLogin
from app.v1.users.register import UserRegister

users_route = Blueprint('users_route', __name__, url_prefix='/api/v1/users/')
users_api = Api(users_route)
users_api.add_resource(UserLogin, 'login')
users_api.add_resource(UserRegister, 'register')
# from app.v1.users.login import *
# from app.v1.users.register import *
