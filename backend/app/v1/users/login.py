"""This file is the login module for the user"""
from flask import make_response, jsonify  # type: ignore
from flasgger.utils import swag_from  # type: ignore
from flask_restful import Resource   # type: ignore
from app.models.storage_engine import storage
from sqlalchemy import text  # type: ignore


class UserLogin(Resource):
    @swag_from('documentation/login.yml')
    def post(self):
        stm = text("SELECT * FROM users")
        data = storage.ge_instance().execute(stm).fetchall()

        # Convert the data into a format that can tbe serialized to JSON
        data_list = [dict(row) for row in data]

        return make_response(jsonify({"success": "User atempt to login",
                                      "data": data_list}), 200)


# @users_route.route("login", methods=['POST'], strict_slashes=False)
# @swag_from('documentation/login.yml')
# def login():
#     return make_response(jsonify({"success": "User atempt to login"}), 200)
