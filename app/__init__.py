from flask import Flask
from config import Config


# Create an instance of Flask
app = Flask(__name__)

# Pull configuration
app.config.from_object(Config)

from app import views
