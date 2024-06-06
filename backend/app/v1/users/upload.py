"""This file is the login module for the user"""
from flask import request  # type: ignore
from flasgger.utils import swag_from  # type: ignore
from flask_restful import Resource   # type: ignore
from app.libs.upload_file import upload_image


class Upload(Resource):
    @swag_from('documentation/login.yml')
    def post(self):
        # stm = text("SELECT * FROM users_account Where email='{}'"
        # .format(str(request.json.get('email'))))
        # data = storage.get_instance().execute(stm).fetchall()
        file = request.files
        return upload_image(file['profile_image'])
