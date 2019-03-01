from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS

from flask_sqlalchemy import SQLAlchemy
from flask_graphql import GraphQLView

from config import Config


# Create an instance of Flask
app = Flask(__name__)

# Pull configuration
app.config.from_object(Config)

# Enable CORS
CORS(app)

# Create pymongo instance
mongo = PyMongo(app)

db = SQLAlchemy(app)

from app import views
from app.schema import schema

app.add_url_rule(
  '/graphql',
  view_func=GraphQLView.as_view(
    'graphql',
    schema=schema,
    graphiql=True
  )
)
