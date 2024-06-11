"""This file is the login module for the user"""

from flasgger.utils import swag_from  # type: ignore
from flask_restful import Resource, marshal_with  # type: ignore
from app.models.storage_engine import storage
from sqlalchemy import select  # type: ignore
from app.models.schemas.users.user import Users
from flask import request  # type: ignore
from app.libs.password import check_password
from app.libs.jwt import encodes_
from app.v1.response_object import response_obj_template


class UserLogin(Resource):
    @marshal_with(response_obj_template)
    @swag_from("documentation/login.yml")
    def post(self):
        body = request.json
        print(body)
        data = storage.get_instance().scalar(
            select(Users).where(Users.email == str(body.get("email")))
        )
        # data = storage.get_instance().query(Users).
        # get({"email": request.json.get('email')})
        # Convert the data into a format that can tbe serialized to JS#ON

        if data is None:
            return {
                "error": "User with email {} not found".format(body.get("email")),
                "success": "",
            }, 400
        pass_check = check_password(body.get("password"), data.password)
        # pa = body.get('password')

        if pass_check is not True:
            return {"error": "Invalid credential", "data": ""}, 400
        json_data = encodes_(data.user_id, data.email)
        # print(data.email,  pass_check, json_data)
        # user_data = decode_(json_data)
        # print(user_data)

        return {"success": "User to login successful", "data": json_data}, 200


# @users_route.route("login", methods=['POST'], strict_slashes=False)
# @swag_from('documentation/login.yml')
# def login():
#     return make_response(jsonify({"success": "User atempt to login"}), 200)
