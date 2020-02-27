import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

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
    item = self.find_by_name(name)
    if item:
      return item
    return {'message': 'Item not found'}, 404

  @jwt_required()
  def post(self, name):
    # if name is found (not None), already exists
    if self.find_by_name(name):
      return { 'message': f"An item with name {name} already exists" }, 400
    
    payload = Item.parser.parse_args()

    item = { 'name': name, 'price': payload['price'] }
    
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    query = "INSERT INTO items VALUES (?, ?)"
    cursor.execute(query, (item['name'], item['price']))
    connection.commit()
    connection.close()

    return item, 201

  @classmethod
  def find_by_name(cls, name):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    query = "SELECT * FROM items WHERE name=?"
    result = cursor.execute(query, (name,))
    row = result.fetchone()
    connection.commit()
    connection.close()

    if row:
      return { 'item': {'name': row[0], 'price': row[1]}}

  @jwt_required()
  def delete(self, name):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    
    query = "DELETE FROM items WHERE name=?"
    cursor.execute(query, (name,))
    
    connection.commit()
    connection.close()
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
