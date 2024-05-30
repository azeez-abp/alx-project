#!/usr/bin/python3
""" Flask Application """
from os import environ
from flask import Flask, make_response, jsonify  # type: ignore
from flask_restful import Resource, Api  # type: ignore
from flask_cors import CORS  # type: ignore
from flasgger import Swagger  # type: ignore
from app.v1.users import users_route
# from flasgger.utils import swag_from
print(__name__, )
app = Flask(__name__)

app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(users_route)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
# parser = reqparse.RequestParser()


@app.teardown_appcontext
def close_db(error):
    """ Close Storage """
    pass
    """storage.close() """


@app.errorhandler(404)
def not_found(error):
    """ 404 Error
    ---
    responses:
      404:
        description: a resource was not found
    """
    return make_response(jsonify({'error': "Not found"}), 404)


app.config['SWAGGER'] = {
    'title': 'AirBnB clone Restful API',
    'uiversion': 3
}


Swagger(app)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        """
        A simple test API
        This ednpoint does nothing
        Only returs "test"

        """
        return {'hello': 'world'}


api.add_resource(HelloWorld, '/')

if __name__ == "__main__":
    """ Main Function """
    host = environ.get('HBNB_API_HOST')
    port = environ.get('HBNB_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'
    app.run(host=host, port=port, threaded=True)
