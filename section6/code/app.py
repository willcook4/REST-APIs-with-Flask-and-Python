from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from datetime import timedelta

from db import db
from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList

PORT = 5000
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # use the sqlalchemy tracker not the flask_sqlalchemy tracker
api = Api(app)
app.secret_key = 'jose'
app.config['JWT_AUTH_URL_RULE'] = '/login' # change the default JWT /auth endpoint to /login 
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800) # set JWT token to expire within 30 min
jwt = JWT(app, authenticate, identity) 

# Student inherits from the Resource class
# class Student(Resource):
#   # get is a class method to handle the matching HTTP Verb GET
#   def get(self, name):
#     return { 'student': name }

### Endpoints
# api.add_resource(Student, '/student/<string:name>') # eg. http://localhost:5000/student/Will

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

# only run this file once. 
if __name__ == "__main__":
  db.init_app(app)
  app.run(port=PORT, debug=True)