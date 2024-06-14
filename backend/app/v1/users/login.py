"""This file is the login module for the user"""

from flasgger.utils import swag_from  # type: ignore
from flask_restful import Resource  # type: ignore
from app.models.storage_engine import storage
from sqlalchemy import select  # type: ignore
from app.models.schemas.users.user import Users
from flask import request, make_response  # type: ignore
from app.libs.password import check_password
from app.libs.jwt import encodes_
# from app.v1.response_object import response_obj_template
from app.libs.cookies import CookieHandler
import uuid
from flask import jsonify  # Import jsonify


class UserLogin(Resource):
    # @marshal_with(response_obj_template)
    @swag_from("documentation/login.yml")
    def post(self):
        body = request.json
        data = storage.get_instance().scalar(
            select(Users).where(Users.email == str(body.get("email")))
        )

        if data is None:
            return {
                "error": "User with email {} not found".
                format(body.get("email")),
                "success": "",
            }, 400

        pass_check = check_password(body.get("password"), data.password)

        if not pass_check:
            return jsonify({"error": "Invalid credential", "data": ""}), 400

        json_data = encodes_(data.user_id, data.email)

        # Create a response object and set the cookie
        response = make_response(jsonify({"success": "User login successful",
                                          "data": json_data}))
        CookieHandler.set_cookie(response, "farm", str(uuid.uuid4()),
                                 60*60*24*7)

        return response
