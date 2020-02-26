from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

from security import authenticate, identity

PORT = 5000
app = Flask(__name__)
api = Api(app)
app.secret_key = 'jose'

jwt = JWT(app, authenticate, identity) # /auth endpoint

# fake db
items = []

# Student inherits from the Resource class
# class Student(Resource):
#   # get is a class method to handle the matching HTTP Verb GET
#   def get(self, name):
#     return { 'student': name }

class Item(Resource):
  # NOTE it is not self.parser, parser belongs to the class not an instance of the clas
  parser = reqparse.RequestParser()
  # We only define price as a parser argument
  # so a user can only set the price of an item:
  parser.add_argument('price', 
    type=float,
    required=True,
    help="This field cannot be left blank")

  # @jwt_required(), decorator means the jwt rquest token must be vaild and provided to use this method
  @jwt_required()
  def get(self, name):
    #  next returns the first item found in the filter function
    # None is the default value
    item = next(filter(lambda x: x['name'] == name, items), None) 
    return { 'item': item }, 200 if item else 404    

  @jwt_required()
  def post(self, name):
    # if name is found (not None), already exists
    if next(filter(lambda x: x['name'] == name, items), None):
      return { 'message': f"An item with name {name} already exists" }, 400
    
    payload = Item.parser.parse_args()

    item = { 'name': name, 'price': payload['price'] }
    items.append(item)
    return item, 201

  @jwt_required()
  def delete(self, name):
    global items # use the global items variable, don't create a local var 
    items = list(filter(lambda x: x['name'] != name, items))
    return { 'message': f"Item deleted: {name}" }

  @jwt_required()
  def put(self, name):
    data = Item.parser.parse_args()

    item = next(filter(lambda x: x['name'] == name, items), None)
    if item is None:
      item = { 'name': name, 'price': data['price'] }
      items.append(item)
    else:
      item.update(data)
    return item

class ItemList(Resource):
  def get(self):
    return { 'items': items }

  
# Endpoints
# api.add_resource(Student, '/student/<string:name>') # eg. http://localhost:5000/student/Will

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

app.run(port=PORT, debug=True)