from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy 
from flask_cors import CORS
app=Flask(__name__)
CORS(app)
api=Api(app)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db = SQLAlchemy(app) 
from backend.routes import Connection ,QueCustomer
api.add_resource(Connection, '/')
api.add_resource(QueCustomer,'/que')