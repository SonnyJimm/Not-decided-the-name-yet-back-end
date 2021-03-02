from flask import Flask
from flask_restful import Api
import sqlite3
from flask_cors import CORS
app=Flask(__name__)
CORS(app)
api=Api(app)
#might be dum solution but it does the trick
db = sqlite3.connect("site.db",check_same_thread=False)

from backend.routes import Connection ,QueCustomer
api.add_resource(Connection, '/')
api.add_resource(QueCustomer,'/que')