"""This file is the login module for the user"""
from flask import make_response, jsonify  # type: ignore
from flasgger.utils import swag_from  # type: ignore
from flask_restful import Resource   # type: ignore
from app.models.storage_engine import storage
from sqlalchemy import select  # type: ignore
from app.models.schemas.users.user import Users
from flask import request  # type: ignore
from app.libs.password import check_password
from app.libs.jwt import encodes_, decode_


class UserLogin(Resource):
    @swag_from('documentation/login.yml')
    def post(self):
        # stm = text("SELECT * FROM users_account Where email='{}'"
        # .format(str(request.json.get('email'))))
        # data = storage.get_instance().execute(stm).fetchall()
        body = request.json
        print(body)
        data = storage.get_instance().scalar(select(Users).
                                             where(Users.email ==
                                                   str(body.get('email'))))
        # data = storage.get_instance().query(Users).
        # get({"email": request.json.get('email')})
        # Convert the data into a format that can tbe serialized to JS#ON
        
        if data is None:
            return make_response(jsonify({"error": f"User with email\
                                          :{body.get('email')} not found",
                                          "data": ""}), 404)
        pass_check = check_password(body.get('password'), data.password)
        # pa = body.get('password')

        if pass_check is not True:
            return make_response(jsonify({"error": "Invalid credential",
                                          "data": ""}), 404)
        json_data = encodes_(data.user_id, data.email)
        # print(data.email,  pass_check, json_data)
        # user_data = decode_(json_data)
        # print(user_data)

        return make_response(jsonify({"success": "User atempt to login",
                                      "data": json_data}), 200)


# @users_route.route("login", methods=['POST'], strict_slashes=False)
# @swag_from('documentation/login.yml')
# def login():
#     return make_response(jsonify({"success": "User atempt to login"}), 200)
