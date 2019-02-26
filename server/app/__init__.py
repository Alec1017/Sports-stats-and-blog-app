from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS

from config import Config


# Create an instance of Flask
app = Flask(__name__)

# Pull configuration
app.config.from_object(Config)

# Enable CORS
CORS(app)

# Create pymongo instance
mongo = PyMongo(app)

from app import views
