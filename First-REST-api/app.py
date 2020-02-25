from flask import Flask, jsonify, request, render_template

port = 5000
app = Flask(__name__) #__name__ provides a unique name to this Flask app object

# sample data as we are not connected to a database
stores = [{
  'name': 'My Wonderful Store',
  'items': [
    {
      'name': 'My Item',
      'price': 15.99
    }
  ]
}]
@app.route('/') # the top-level endpoint
def home():
#   return "Hello World!"
  return render_template('index.html')

# POST /store data: {name: }
@app.route('/store', methods=['POST'])
def create_store():
  request_data = request.get_json()
  new_store = {
    'name': request_data['name'],
    'items': []
  }
  stores.append(new_store)
  return jsonify(new_store)

# GET  /store/<string:name>
@app.route('/store/<string:name>', methods=['GET'])
def get_store(name):
  for store in stores:
    if store['name'] == name: 
      return jsonify(store)
    return jsonify({ 'message': f"Store {name} not found" })
  
# GET /stores
@app.route('/stores', methods=['GET'])
def get_stores():
  return jsonify({ 'stores': stores })

# POST /store/<string:name>/item
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
  request_data = request.get_json()
  for store in stores:
    if store['name'] == name:
      new_item = {
        'name': request_data['name'],
        'price': request_data['price'],
      }
      store['items'].append(new_item)
      return jsonify(store)
    return jsonify({ 'message': f"store name {name} not found"})

# GET /store/<string:name>/items
@app.route('/store/<string:name>/items', methods=['GET'])
def get_items_in_store(name):
  for store in stores:
    if store['name'] == name:
      return jsonify({ 'items': store['items'] })
    else: 
      return jsonify({ 'message': f"store name {name} not found"})

app.run(port=port)