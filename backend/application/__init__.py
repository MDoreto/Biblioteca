from flask import Flask,jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from .config import Config


app = Flask(__name__)
app.config.from_object(Config)
jwt = JWTManager(app)
CORS(app,
     supports_credentials=True)


@jwt.token_verification_failed_loader
def my_expired_token_callback(jwt_headers, jwt_payload):
    return jsonify(code="dave", err="I can't let you do that"), 405


import application.routes
