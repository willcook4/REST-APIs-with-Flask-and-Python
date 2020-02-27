import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

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
    item = ItemModel.find_by_name(name)
    if item:
      return item.json()
    return {'message': 'Item not found'}, 404

  @jwt_required()
  def post(self, name):
    # if name is found (not None), already exists
    if ItemModel.find_by_name(name):
      return { 'message': f"An item with name {name} already exists" }, 400
    
    payload = Item.parser.parse_args()

    item = ItemModel(name, payload['price'])
    try:
      ItemModel.insert(item)
    except:
      return {'message': 'An error occurred inserting the item'}, 500
    return item.json(), 201

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

    item = ItemModel.find_by_name(name)
    updated_item = ItemModel(name, data['price'])
    
    if item is None:
      try:
        updated_item.insert()
      except:
        return {'message': 'an error occured inserting the item'}, 500
    else:
      try:
        updated_item.update()
      except:
        return {'message': 'an error occured inserting the item'}, 500
    
    return updated_item.json()

class ItemList(Resource):
  def get(self):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    
    query = "SELECT * FROM items"
    result = cursor.execute(query)
    items = []
    for row in result:
      items.append({'name': row[0], 'price': row[1]})

    connection.commit()
    connection.close()

    return { 'items': items }
