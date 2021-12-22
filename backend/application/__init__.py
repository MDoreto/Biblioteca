from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from .config import Config


app = Flask(__name__)
app.config.from_object(Config)
jwt = JWTManager(app)
CORS(app,resources={r"/*": {"origins": "*"}},
     supports_credentials=True)

import application.routes
