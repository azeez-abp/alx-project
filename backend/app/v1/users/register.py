from flask import request  # type: ignore
from flasgger.utils import swag_from  # type: ignore
from flask_restful import (Resource,  # type: ignore
                           reqparse,
                           fields,
                           marshal_with)
from app.models.schemas.users.user import Users
from app.models.schemas.general.address import Addresses
from app.libs.password import hash_password
import uuid

# Define the expected structure for success and error responses
response_obj_template = {
    'success': fields.String,
    'user_id': fields.String,
    'email': fields.String,
    'error': fields.String(attribute='error')
    # This line is only to illustrate the structure
}


# Define a resource class for user registration
class UserRegister(Resource):
    """Class for registering a user."""
    @swag_from('documentation/register.yml')
    @marshal_with(response_obj_template, envelope='response')
    def post(self):
        parser = reqparse.RequestParser()
        # Validate input
        parser.add_argument('first_name', type=str, required=True,
                            help='First name must be a \
                                string and cannot be blank')
        parser.add_argument('last_name', type=str, required=True,
                            help='Last name must be a \
                                string and cannot be blank')
        parser.add_argument('email', type=str, required=True,
                            help='Email must be a string and cannot be blank')
        parser.add_argument('password', type=str, required=True,
                            help='Password must be a \
                                string and cannot be blank')
        parser.add_argument('file', type=str, required=False)
        data_all = request.get_json()
        user_id = uuid.uuid4()
        new_address = Addresses(
            user_id=user_id,
            street=data_all['street'],
            city=data_all['city'],
            state=data_all['state'],
            zip_code=data_all['zip_code']
        )
        new_user = Users(
            user_id=user_id,
            first_name=data_all['first_name'],
            profile_pix=data_all['profile_pix'],
            middle_name=data_all['middle_name'],
            last_name=data_all['last_name'],
            email=data_all['email'],
            password=hash_password(data_all['password']),
            gender=data_all['gender'],
            date_of_birth=data_all['date_of_birth'],
            addresses=[new_address]
        )
        try:
            Users.add([new_user])
            response = {
                'success': 'User successfully registered',
                'user_id': str(user_id),
                'email': data_all['email'],
                'error': ''
            }
            return response, 201
        except Exception as e:
            error_response = {
                'success': '',
                'data': {},
                'error': f'User registration failed {e._message}'
            }
            return error_response, 400
