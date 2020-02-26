from flask import Flask, request
from flask_restful import Resource, Api

PORT = 5000
app = Flask(__name__)
api = Api(app)

# fake db
items = []

# Student inherits from the Resource class
class Student(Resource):
  # get is a class method to handle the matching HTTP Verb GET
  def get(self, name):
    return { 'student': name }

class Item(Resource):
  def get(self, name):
    for item in items:
      if item['name'] == name:
        return item
    return { 'message': f"no items found with {name}" }, 404

  def post(self, name):
    payload = request.get_json()
    item = { 'name': name, 'price': payload['price'] }
    items.append(item)
    return item, 201

class ItemList(Resource):
  def get(self):
    return { 'items': items }

  
# Endpoints
api.add_resource(Student, '/student/<string:name>') # eg. http://localhost:5000/student/Will

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

app.run(port=PORT, debug=True)